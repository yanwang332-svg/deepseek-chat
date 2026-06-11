# -*- coding: utf-8 -*-
import os
os.environ["PYTHONUTF8"] = "1"
os.environ["PYTHONIOENCODING"] = "utf-8"

import json
import ssl
import time
import streamlit as st
import http.client
import certifi
from urllib.parse import urlparse
from datetime import datetime
import base64

# ====================== 本地存储目录 ===========================
CONFIG_DIR = os.path.expanduser("~/.deepseek_chat")
SECRET_FILE = os.path.join(CONFIG_DIR, "api_key.enc")
LOG_FILE = os.path.join(CONFIG_DIR, "chat_log.jsonl")

# ====================== 本地文件操作（Cloud 上自动降级） ===========================
def _safe_write(filepath, data, mode="w"):
    """Cloud 上文件系统只读时静默跳过"""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, mode) as f:
            f.write(data)
        return True
    except (OSError, PermissionError):
        return False  # Cloud 环境，静默跳过

def _safe_read(filepath, mode="r"):
    try:
        if os.path.exists(filepath):
            with open(filepath, mode) as f:
                return f.read()
    except (OSError, PermissionError):
        pass
    return None

# 优先用 cryptography 真加密，不可用则降级为 base64
try:
    from cryptography.fernet import Fernet
    KEY_FILE = os.path.join(CONFIG_DIR, ".key")

    def _get_fernet():
        try:
            os.makedirs(CONFIG_DIR, exist_ok=True)
        except OSError:
            return None
        if os.path.exists(KEY_FILE):
            key = _safe_read(KEY_FILE, "rb")
            if key:
                return Fernet(key)
        key = Fernet.generate_key()
        if _safe_write(KEY_FILE, key, "wb"):
            try:
                os.chmod(KEY_FILE, 0o600)
            except OSError:
                pass
        return Fernet(key)

    def _encrypt(text):
        f = _get_fernet()
        return f.encrypt(text.encode()) if f else base64.b64encode(text.encode())

    def _decrypt(data):
        f = _get_fernet()
        return f.decrypt(data).decode() if f else base64.b64decode(data).decode()

except ImportError:
    def _encrypt(text):
        return base64.b64encode(text.encode())
    def _decrypt(data):
        return base64.b64decode(data).decode()

def save_api_key(api_key):
    data = _encrypt(api_key)
    _safe_write(SECRET_FILE, data, "wb")

def load_api_key():
    data = _safe_read(SECRET_FILE, "rb")
    if data is None:
        return None
    try:
        return _decrypt(data)
    except Exception:
        return None

# ====================== 对话日志（Cloud 上自动跳过） ===========================
def save_log(role, content):
    entry = json.dumps({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "role": role,
        "content": content,
    }, ensure_ascii=False)
    _safe_write(LOG_FILE, entry + "\n", "a")

def load_logs(limit=100):
    data = _safe_read(LOG_FILE, "r")
    if data is None:
        return []
    logs = []
    for line in data.strip().split("\n"):
        if line.strip():
            try:
                logs.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return logs[-limit:]

st.set_page_config(page_title="DeepSeek 聊天助手", page_icon="🤖", layout="wide")

# ====================== API Key 安全读取 ===========================
def get_api_key():
    # 1. Streamlit Cloud Secrets
    try:
        return st.secrets["DEEPSEEK_API_KEY"]
    except (KeyError, FileNotFoundError):
        pass
    # 2. 系统环境变量
    env_key = os.getenv("DEEPSEEK_API_KEY")
    if env_key:
        return env_key
    # 3. 本地加密存储
    local_key = load_api_key()
    if local_key:
        return local_key
    return None

server_api_key = get_api_key()
is_saved = server_api_key is not None  # 是否有现成的 Key（不论来源）

# ====================== 侧边栏配置 ===========================
with st.sidebar:
    st.header("⚙️ 配置")

    if is_saved:
        api_key = server_api_key
        try:
            _ = st.secrets["DEEPSEEK_API_KEY"]
            source = "Secrets"
        except (KeyError, FileNotFoundError):
            source = "环境变量" if os.getenv("DEEPSEEK_API_KEY") else "本地加密存储"
        st.success(f"✅ Key 已加载（来源：{source}）")
        # 允许手动覆盖
        new_key = st.text_input("更换 Key（留空则使用已保存的）", type="password")
        if new_key:
            try:
                new_key.encode("ascii")
                api_key = new_key
                save_api_key(new_key)
                st.info("已保存新 Key 到本地")
            except UnicodeEncodeError:
                st.warning("Key 含有非英文字符，未保存")
    else:
        # 生产环境自动引导，本地给手动选项
        if IS_PROD:
            st.info("☁️ 请在 App Settings → Secrets 中配置 Key，然后刷新页面")
            api_key = ""
        else:
            # 本地用户引导
            st.warning("⚠️ 未检测到已保存的 Key")
            st.caption("运行以下命令配置（不经过前端）：")
            st.code(f"echo 'sk-你的key' |  python3 -c \"import sys; from cryptography.fernet import Fernet; import os; d=os.path.expanduser('~/.deepseek_chat'); os.makedirs(d,exist_ok=True); k=Fernet.generate_key(); open(d+'/.key','wb').write(k); open(d+'/api_key.enc','wb').write(Fernet(k).encrypt(sys.stdin.read().strip().encode()))\"", language="bash")
            st.caption("或手动输入：")
            api_key = st.text_input("DeepSeek API Key", type="password")
            if api_key and len(api_key) > 10:
                try:
                    api_key.encode("ascii")
                    save_api_key(api_key)
                except UnicodeEncodeError:
                    pass

    base_url = st.text_input("API Base URL", value="https://api.deepseek.com", help="默认使用官方地址")
    model_name = st.selectbox("模型", ["deepseek-chat", "deepseek-reasoner","deepseek-v4-pro"], index=0)
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.05, help="控制回答的随机性/创造性")
    max_tokens = st.slider("Max Tokens", 512, 4096, 2048, 128, help="限制回答的最大 token 数")

    if st.button("🧹 清空历史对话"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    # 历史日志（仅本地开发显示，部署后隐藏）
    if not IS_PROD:
        with st.expander("📋 对话日志", expanded=False):
            logs = load_logs(50)
            if logs:
                for log in reversed(logs):
                    icon = "🧑" if log["role"] == "user" else "🤖"
                    content = log["content"][:80] + ("..." if len(log["content"]) > 80 else "")
                    st.caption(f"{icon} {log['time']}  {content}")
            else:
                st.caption("暂无日志")

    st.markdown("---")
    st.caption("DeepSeek API 兼容 OpenAI 接口")

# ====================== 初始化 ===========================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "last_request_time" not in st.session_state:
    st.session_state.last_request_time = 0
if "request_count" not in st.session_state:
    st.session_state.request_count = 0

# ====================== 门禁密码 ===========================
# Cloud 检测：DEEPSEEK_API_KEY 在 Secrets 中说明已部署
try:
    _ = st.secrets["DEEPSEEK_API_KEY"]
    IS_PROD = True  # 生产环境，隐藏敏感信息
except (KeyError, FileNotFoundError):
    IS_PROD = False  # 本地开发

try:
    ACCESS_PASSWORD = st.secrets["APP_PASSWORD"]
except (KeyError, FileNotFoundError):
    ACCESS_PASSWORD = ""

st.markdown("<h1 style='text-align: center;'>💬 DeepSeek 聊天框</h1>", unsafe_allow_html=True)

if not st.session_state.unlocked:
    st.markdown("<div style='text-align: center; color: #888;'>请输入访问密码</div>", unsafe_allow_html=True)
    pwd = st.text_input("密码", type="password", key="pwd_input")

    # 验证密码：优先用 Secrets 里配的 APP_PASSWORD，没配则用默认 888888
    correct_pwd = ACCESS_PASSWORD if ACCESS_PASSWORD else "888888"
    if pwd == correct_pwd:
        st.session_state.unlocked = True
        st.success("✅ 验证通过")
        st.rerun()
    elif pwd and pwd != correct_pwd:
        st.error("密码错误，请重试")
    st.stop()

# ====================== 已解锁：正常聊天 ======================
st.markdown("<div style='text-align: center; color: #888;'>与 DeepSeek 大模型对话，支持上下文记忆</div>", unsafe_allow_html=True)

# 显示使用统计
col1, col2 = st.columns(2)
with col1:
    st.caption(f"📊 本次会话请求：{st.session_state.request_count}")
with col2:
    st.caption("🛡️ 间隔限制：3秒")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ====================== 处理用户输入 ===========================
if user_input := st.chat_input("请输入你的问题"):
    if not api_key:
        st.error("请在左侧边栏输入您的 DeepSeek API Key")
        st.stop()

    try:
        api_key.encode("ascii")
    except UnicodeEncodeError:
        st.error("API Key 只能包含英文字母和数字，请检查是否误输入了中文")
        st.stop()

    # 频率限制：至少间隔 3 秒
    now = time.time()
    elapsed = now - st.session_state.last_request_time
    if elapsed < 3:
        st.warning(f"请稍等 {3 - elapsed:.0f} 秒后再发送")
        st.stop()

    st.session_state.request_count += 1
    st.session_state.last_request_time = now

    st.session_state.messages.append({"role": "user", "content": user_input})
    save_log("user", user_input)
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        messages_to_send = st.session_state.messages[-20:]
        payload = {
            "model": model_name,
            "messages": messages_to_send,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False,
        }
        body_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")

        parsed = urlparse(base_url)
        host = parsed.netloc or "api.deepseek.com"
        ssl_ctx = ssl.create_default_context(cafile=certifi.where())

        conn = http.client.HTTPSConnection(host, timeout=60, context=ssl_ctx)
        conn.request(
            "POST", "/v1/chat/completions",
            body=body_bytes,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json; charset=utf-8",
            },
        )
        resp = conn.getresponse()
        data = json.loads(resp.read().decode("utf-8"))

        if "error" in data:
            st.error(f"API 错误：{data['error'].get('message', data['error'])}")
            st.stop()

        assistant_response = data["choices"][0]["message"]["content"]

        save_log("assistant", assistant_response)
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        st.error(f"请求出错：{e}")
