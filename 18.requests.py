import csv
import re
import tempfile
from sqlite3 import converters
from wsgiref import headers
from xml.etree.ElementTree import C14NWriterTarget

import requests
url = "http://ww.baidu.com"
response = requests.get(url)
# response.encoding = "utf8"
# 打印源码的str类型数据
# print(response.text)

# repones.content是存储bytes类型的响应源码，可以进行decode操作
# print(response.content.decode())


# 常见的响应对象参数和方法
# 响应url
# print(response.url)

# 状态码
# print(response.status_code)

# 响应对应的请求头
# print(response.request.headers)
# 响应头
# print(response.headers)

# 答应响应设置cookies
# print(response.cookies)
# 自动将json字符串类型的响应内容转化为python对象（dict or list）
# print(response.json)

# 构建请求头字典
headers = {
    "user-agent":
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
# 发送请求头的请求
# response1 = requests.get(url, headers=headers)
#
# print(len(response1.content.decode()))
# print(response1.content.decode())

# 测试

# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
#
# try:
#     resp = requests.get(f"{url}/1",timeout=10)
#     resp.raise_for_status()
#     print("get 成功")
#     print(resp.json())
# except Exception as e:
#     print(f"响应失败:{e}")


# # 题目 1：获取并打印一条名人名言
# import requests
# url = "http://v1.hitokoto.cn/"
# # 使用 requests.get 请求该 API，设置 5 秒超时。
# try:
#     resp = requests.get(f"{url}", timeout=5)
#     resp.raise_for_status()
#     data = resp.json()
#     print("get 成功")
#     # 解析返回的 JSON，提取 content 和 author。
#     print(f"内容:{data['hitokoto']}")
#     print(f"出处：{data.get('from','未知出处')}")
# except Exception as e:
#     print(f"获取失败：{e}")


# # 题目 2：批量获取并保存用户信息（CSV）
# #
# # 目标：练习 GET 请求、循环、文件写入（csv模块）。
# #
# # API 接口：https://jsonplaceholder.typicode.com/users （免费，返回10个用户的JSON列表）
#
# import requests
# from pathlib import Path
# import json
# import csv
#
# url = "https://jsonplaceholder.typicode.com/users"
# # 请求该 API，获取所有用户列表。
# try:
#     resp = requests.get(url, timeout=10)
#     datas = resp.json()
#     resp.raise_for_status()
#     # 遍历每个用户，提取name、email、address.city
#     with open("data.csv", "w",newline = "" ,encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(["姓名","邮箱","城市"])
#         for data in datas:
#             name = data["name"]
#             email = data["email"]
#             city = data["address"]["city"]
#             writer.writerow([name,email,city])
#         print(f"成功写入{len(datas)}条记录")
#
#
# except Exception as e:
#     print(e)


# 题目 3 – 命令行天气查询工具
# 用户通过命令行输入城市名称，例如 python weather.py 呼和浩特
# 调用免费天气 API（推荐 wttr.in 或 https://api.open-meteo.com）获取当前温度、天气描述、湿度
# 打印友好格式的天气信息
# 将每次查询记录追加到

# import requests
# import sys
# import json
# from datetime import datetime
#
#
# def get_weather(city_name):
#     """
#
#     :param city_name: 城市名称
#     :return:温度，天气描述，湿度，或者none值
#     """
#     URL= f"https://wttr.in/{city_name}?format=j1"
#     try:
#         resp = requests.get(URL,timeout=10)
#         resp.raise_for_status()
#         date = resp.json()
#         current = date["current_condition"][0]
#         temp = current["temp_C"]
#         desc = current["weatherDesc"][0]["value"]
#         humidity = current["humidity"]
#         return temp, desc, humidity
#     except requests.exceptions.Timeout:
#         print("错误：请求超时，请检查网络后重试。")
#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP 错误：{e}（城市名可能无效）")
#     except (KeyError, IndexError, json.JSONDecodeError) as e:
#         print(f"解析天气数据失败：{e}（API 返回格式异常）")
#     except Exception as e:
#         print(f"未知错误：{e}")
#     return None
# def save_log(city, temp, desc, humidity):
#     try:
#         with open('weather_log.txt', 'a', encoding='utf-8') as f:
#             timestemp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             f.write(f"{timestemp}|{city}|{temp}°C｜{desc}｜{humidity}%\n")
#     except Exception as e:
#         print(f"写入日记失败，{e}")
#
# def main():
#
#     city = input("请输入要查询的城市：").strip()
#     if not city:
#         city = "北京"
#         print(f"未输入城市默认城市为:{city}")
#
#
#     result = get_weather(city)
#     if result is None :
#         print("天气查询失败，请检查城市名或网络")
#         return
#     temp, desc, humidity = result
#
#     print("\n" + "=" * 30)
#     print(f"【{city}】当前天气")
#     print("=" * 30)
#     print(f"🌡️ 温度：{temp}°C")
#     print(f"☁️ 描述：{desc}")
#     print(f"💧 湿度：{humidity}%")
#     print("=" * 30 + "\n")
#
#     save_log(city, temp, desc, humidity)
#     print("查询结果已保存到：weather_log.txt")



# 题目 4：货币汇率查询工具
"""功能要求
用户输入源货币和目标货币的代码（例如 USD CNY），以及金额。
调用免费汇率 API（推荐使用 https://api.exchangerate-api.com/v4/latest/USD，无需 API Key，但注意国内访问可能稍慢；备选：https://api.exchangerate.host/latest?base=USD）。
获取实时汇率，计算兑换后的金额。
打印结果，格式如：100 USD = 718.50 CNY。
将每次查询记录（时间、源货币、目标货币、金额、结果）追加写入 exchange_log.txt。
处理异常：网络错误、货币代码无效、返回数据缺失等。"""


import requests
import json
def show_all_currencies():
    """获取并打印所有可用的货币代码"""
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # 以 USD 为基准获取所有汇率
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        rates = data.get("rates")
        if rates:
            print("支持的货币代码列表（部分）：")
            # 每行打印 10 个，便于查看
            currencies = list(rates.keys())
            for i in range(0, len(currencies), 10):
                print("  ".join(currencies[i:i+10]))
        else:
            print("无法获取货币列表")
    except Exception as e:
        print(f"获取货币列表失败：{e}")

def get_exchange_rate(base_currency, target_currency):
  """
  
  :param base_currency: 获取的汇率
  :param base_currency_code: 输出的汇率
  :return: 换算汇率后的价钱，失败返回None
  """
  url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
  try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()
      date = response.json()
      rata = date["rates"].get(target_currency)
      if rata is None:
          print(f'错误，不支持目标汇率{target_currency}')
          return None
      else:
          return rata
  except Exception as e:
      print(f"获取汇率失败：{e}")
      return None

def main():
    show_all_currencies()
    base = input("请输入源货币代码：").strip().upper()
    target = input("请输入目标货币代码").strip().upper()
    amount = input("请输入货币金额")

    try:
        amount = float(amount)
    except ValueError:
        print("必须全为数字")

    rate = get_exchange_rate(base, target)
    if rate is  None:
        return

    converted = amount * rate
    print(f"{amount}|{base} = {converted:.2f}|{target}")





if __name__ == '__main__':
    main()
