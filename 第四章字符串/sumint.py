# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/9 7:44
# @Author   : tangky
# @Site     : 
# @File     : sumint.py
# @Software : PyCharm

# 求出一个Python程序里出现的所有整数之和
# 注意,Python把一元的正负号看作运算符,不是整数的一部分
import re


def sumInt(fname):
    re_int = r'\b(0|[1-9]\d*)\b'
    inf = open(fname, encoding='utf-8')
    if not inf:
        return 0
    int_list = map(int, re.findall(re_int, inf.read()))
    # 也可以修改,改用分行读入的方式
    s = 0
    for n in int_list:
        s += n
    return s


if __name__ == '__main__':
    print(sumInt('naive_matching.py'))
