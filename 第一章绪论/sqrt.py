# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/29 10:05
# @Author   : tangky
# @Site     : 
# @File     : sqrt.py
# @Software : PyCharm

def sqrt(x):
    y = 1.0
    while abs(y * y - x ) > 1e-6:
        y = (y + x/y)/2
    return y

print(sqrt(1000))
