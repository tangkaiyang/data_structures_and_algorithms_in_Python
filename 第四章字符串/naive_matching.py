# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/7 8:09
# @Author   : tangky
# @Site     : 
# @File     : naive_matching.py
# @Software : PyCharm

# 朴素串匹配算法


def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1


def matching_KMP(t, p, pnext):
    """KMP串匹配,主函数."""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1
