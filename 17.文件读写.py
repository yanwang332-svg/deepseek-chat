# from pathlib import Path
#
# path = Path("demo.txt")
#
# # 写
# path.write_text("Hello\n世界\n", encoding="utf-8")
#
# # 读
# print(path.read_text(encoding="utf-8"))
#
# # 追加
# with path.open("a", encoding="utf-8") as f:
#     f.write("追加一行\n")
#     f.write("hello, world\n")
# # 再读
# print(path.read_text(encoding="utf-8"))
import json
import os
from datetime import date



# f = open(r"/Users/wangyanmac/Desktop/demo.txt")
# print(f)
# print(f.read(3))
# print(f.name)
# f = open(r"/Users/wangyanmac/PycharmProjects/PythonProject/第二章/demo.txt")
# print(f.read())
# with open("demo.txt",encoding="utf-8") as f :
#     print(f.read())
# with open("/Users/wangyanmac/Desktop/微信图片_20260502200011_499_113.jpg","rb") as f :
#     img = f.read()
#     print(img)
# with open("/Users/wangyanmac/PycharmProjects/PythonProject/第二章/微信图片_20260502200011_499_113.jpg","wb") as f :
#     f.write(img)
# import os
# os.rename("text.txt","demo.txt")
# with open("demo.txt","r",encoding="utf-8")as f:
#     print(f.read())
# from pathlib import Path
# import json
# path = Path("use_info.josh")
#
# if path.exists():
#     contents = path.read_text()
#     user = json.loads(contents)
#     print(f"欢迎回来，您的名字是：{user["name"]}")
#     print(f"欢迎回来，您的名字是：{user["age"]}")
# else:
#     user = {}
#     user["name"] = input("请输入您的名字：")
#     user["age"] = int(input("请输入您的年龄："))
#     contents = json.dumps(user)
#     path.write_text(contents,encoding="utf-8")
#     print(f"信息已录入到{path}文件中！！！")

"""
欢迎使用规范关键词管理器
请选择操作: 1-添加/更新关键词  2-查看分类关键词  3-搜索关键词  4-退出
> 1
请输入分类名: 尺寸规范
请输入关键词(用逗号分隔): 人行道宽度,路缘石高度,树池尺寸
已保存。

请选择操作: 1-添加/更新关键词  2-查看分类关键词  3-搜索关键词  4-退出
> 1
请输入分类名: 尺寸规范
请输入关键词(用逗号分隔): 路缘石高度,台阶高度
已合并新增关键词。

请选择操作: 2
请输入分类名: 尺寸规范
尺寸规范下的关键词: 人行道宽度, 路缘石高度, 树池尺寸, 台阶高度

请选择操作: 3
请输入要搜索的关键词: 高度
关键词"高度"出现在以下分类中:
- 尺寸规范: 路缘石高度, 台阶高度

请选择操作: 4
再见。"""
#
# from pathlib import Path
# import json
# path = Path(keywords.json)
# # class SpecInfo:
# #     def __init__(self,spec_name,spec_info):
# #         self.spec_name = spec_name
# #         self.spec_info = spec_info
#
# def read_spec_info(path):
#     contents = path.read_text()
#     spec_info = json.loads(contents)
#     print(f"您要查询的规范信息是{spec_info["name"]}")
#


import json
from pathlib import Path

KEYWORDS_FILE = Path("keywords.json")

def load_keywords():
    if KEYWORDS_FILE.exists():
        with open(KEYWORDS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def save_keywords(data):
    with open(KEYWORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_keywords(category, new_keywords):
    data = load_keywords()
    if category not in data:
        data[category] = []
    # 合并去重
    existing = set(data[category])
    for kw in new_keywords:
        existing.add(kw)
    data[category] = list(existing)
    save_keywords(data)
    print("已保存。")

def view_category(category):
    data = load_keywords()
    if category in data:
        print(f"{category}下的关键词: {', '.join(data[category])}")
    else:
        print("分类不存在。")

def search_keyword(keyword):
    data = load_keywords()
    found = False
    for cat, kws in data.items():
        if any(keyword in kw for kw in kws):  # 包含子串即可
            print(f"- {cat}: {', '.join([kw for kw in kws if keyword in kw])}")
            found = True
    if not found:
        print("未找到包含该关键词的分类。")

def main():
    while True:
        print("\n请选择操作: 1-添加/更新关键词  2-查看分类关键词  3-搜索关键词  4-退出")
        choice = input("> ").strip()
        if choice == "1":
            cat = input("请输入分类名: ").strip()
            kws = [k.strip() for k in input("请输入关键词(用逗号分隔): ").split(",")]
            add_keywords(cat, kws)
        elif choice == "2":
            cat = input("请输入分类名: ").strip()
            view_category(cat)
        elif choice == "3":
            kw = input("请输入要搜索的关键词: ").strip()
            search_keyword(kw)
        elif choice == "4":
            print("再见。")
            break
        else:
            print("无效输入，请重新选择。")

if __name__ == "__main__":
    main()