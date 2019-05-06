# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/6 6:48
# @Author   : tangky
# @Site     : 
# @File     : list_sort.py
# @Software : PyCharm


def list_sort(lst):
    for i in range(1, len(lst)):  # 开始时片段[0:1]已排序
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1] > x:
            lst[j] = lst[j - 1]  # 反序逐个后移元素至确定插入位置
            j -= 1
        lst[j] = x
