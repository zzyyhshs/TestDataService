#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
======================
@File:api.py
@Author:mayxxiao
@E-mail:mayxxiao@tencent.com,xyyy1227@163.com
@Time:2024/6/18 14:19
@Function:
@Action:
======================
"""
import math
import threading

from flask import Flask, jsonify, request
import random
import datetime
import string

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 解决中文乱码问题


def get_random_data(index, start_num: int, end_num: int, char_count: int, chars: str, start_date: str, end_date: str, date_fmt: str, data_text: str):
    # def get_random_data(index, num, char_count: int = 10, chars: str = '汉字的一些示例文本！@#$%^&*()_+-=[]{}|;:,.<>?/`~',
    #                     start_date: str = '2015-01-01', end_date: str = '2024-5-31'):

    def _get_random_char(char_count: int, chars: str):
        # 生成包含中英文字符及特殊字符的随机字符串
        # 定义包含中英文字符及特殊字符的字符串
        all_chars = string.ascii_letters + string.digits + chars
        return ''.join(random.choices(all_chars, k=char_count))

    def _get_random_date(start: str, end: str, date_fmt: str):
        # 设置时间范围
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        delta = end_date - start_date
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        random_date = start_date + datetime.timedelta(seconds=random_second)
        return random_date.strftime(date_fmt)

    def _get_random_province():
        # 从省份列表中随机选择一个省份名称
        # 中国省份名称列表
        provinces = [
            "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏",
            "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西",
            "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏",
            "新疆"
        ]
        return random.choice(provinces)

    def _get_random_int(start_num, end_num):
        return random.randint(start_num, end_num)

    def _get_random_float(start_num, end_num):
        return random.uniform(start_num, end_num)

    return {
        "id": index,
        "data_int": _get_random_int(start_num, end_num),
        "data_float": _get_random_float(start_num, end_num),
        "data_time": _get_random_date(start_date, end_date, date_fmt),
        "data_char": _get_random_char(char_count, chars),
        "data_province": _get_random_province(),
        "data_nothing": None,
        "data_text": data_text
    }


@app.route('/api/data', methods=['GET'])
def my_get_data():
    # 生成的数据总长度，默认长度：1000
    count = request.args.get(key='count', default=100, type=int)
    # data_int和data_float字段的随机数范围下限，默认：0
    start_num = request.args.get(key='startNum', default=0, type=int)
    # data_int和data_float字段的随机数范围上限，默认：100000
    end_num = request.args.get(key='endNum', default=100000, type=int)
    # name字段的字符串长度，默认：10
    char_count = request.args.get(key='charCount', default=10, type=int)
    # name字段的随机字符，默认：汉字的一些示例文本！@#$%^&*()_+-=[]{}|;:,.<>?/`~
    chars = request.args.get(key='chars', default='汉字的一些示例文本！@#$%^&*()_+-=[]{}|;:,.<>?/`~', type=str)
    # timestamp字段的随机时间范围的开始时间，默认：2015-01-01
    start_date = request.args.get(key='startDate', default='2015-01-01', type=str)
    # timestamp字段的随机时间范围的结束时间，默认：2024-5-31
    end_date = request.args.get(key='endDate', default='2024-5-31', type=str)
    # timestamp字段返回的时间格式，默认：%Y-%m-%d %H:%M:%S
    date_fmt = request.args.get(key='dateFmt', default='%Y-%m-%d %H:%M:%S', type=str)
    # 返回的分页数，默认：None，不分页
    start_page = request.args.get(key='startPage', default=None, type=int)
    # 分页时一页返回的数据量，默认：100
    page_size = request.args.get(key='pageSize', default=100, type=int)
    #
    data_text = request.args.get(key='text', default="NULL", type=str)

    start = 0

    if start_page is not None and page_size is not None:
        start = (start_page - 1) * page_size
        end = start_page * page_size
        if start > count:
            return "超出最大翻页数，最大页数：%s" % math.ceil(count/page_size)
        if end < count:
            count = end

    data = list()
    for i in range(start+1, count+1):
        data.append(get_random_data(index=i, start_num=start_num, end_num=end_num, char_count=char_count,
                                    chars=chars, start_date=start_date, end_date=end_date, date_fmt=date_fmt,
                                    data_text=data_text))
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=8080)