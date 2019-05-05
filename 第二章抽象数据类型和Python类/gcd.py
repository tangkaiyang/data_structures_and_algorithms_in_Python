# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/30 10:07
# @Author   : tangky
# @Site     : 
# @File     : gcd.py
# @Software : PyCharm


# 最大公约数
def gcd(m, n):
    if n == 0:
        m, n = n, m
    while m != 0:
        m, n = n % m, m
    return n


print(gcd(36, 54))
