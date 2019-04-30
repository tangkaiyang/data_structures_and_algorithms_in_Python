# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/30 15:58
# @Author   : tangky
# @Site     : 
# @File     : cls_counter.py
# @Software : PyCharm

# 计数器
class Countable:
    counter = 0

    def __init__(self):
        Countable.counter += 1

    @classmethod
    def get_count(cls):
        return Countable.counter


x = Countable()
y = Countable()
z = Countable()

print(Countable.get_count())
