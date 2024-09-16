import json
import random
from datetime import datetime

def read_feminist_data():
    try:
        with open('feminist_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        # print("读取的数据列表：")
        print(data)
        return data
    except FileNotFoundError:
        print("错误：找不到 feminist_data.json 文件")
        return []
    except json.JSONDecodeError:
        print("错误：无法解析 JSON 数据")
        return []


import datetime
import random

def get_zodiac_sign(birthday):
    # 将生日字符串转换为日期对象
    birth_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    month = birth_date.month
    day = birth_date.day
    
    # 定义星座日期范围
    zodiac_dates = [
        (1, 20, "摩羯座"), (2, 19, "水瓶座"), (3, 21, "双鱼座"), (4, 20, "白羊座"),
        (5, 21, "金牛座"), (6, 22, "双子座"), (7, 23, "巨蟹座"), (8, 23, "狮子座"),
        (9, 23, "处女座"), (10, 24, "天秤座"), (11, 23, "天蝎座"), (12, 22, "射手座"),
        (12, 31, "摩羯座")  # 添加年末边界条件
    ]
    
    # 确定星座
    for i, (end_month, end_day, sign) in enumerate(zodiac_dates):
        if (month < end_month) or (month == end_month and day <= end_day):
            return sign
    
    return "摩羯座"  # 如果是12月23日至31日，返回摩羯座

def find_matching_feminist(birthday, feminist_data):
    user_zodiac = get_zodiac_sign(birthday)
    matching_feminists = [feminist for feminist in feminist_data if feminist["星座"] == user_zodiac]
    
    if matching_feminists:
        return random.choice(matching_feminists)
    else:
        return None

# 测试代码
test_birthday = "1998-04-25"
feminist_data = read_feminist_data()  # 假设这个函数已经定义并可以正确读取数据
result = find_matching_feminist(test_birthday, feminist_data)
print("匹配的女性主义者数据：")
print(result)

