# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/30 10:32
# @Author   : tangky
# @Site     : 
# @File     : rational.py
# @Software : PyCharm


# 有理数类
class Rational:
    @staticmethod
    def _gcd(m, n):
        if m == 0:
            return m
        while n != 0:
            n, m = m, m % n
        return m
