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


def gen_pnext(p):
    # pnext = [0 for i in range(len(p))]
    # pnext[0] = -1
    # i = 0
    # while i < len(pnext):
    #     i += 1
    #     if pnext[i-1]+1 == -1:
    #
    #     if p[i] == p[pnext[i-1]+1]:
    #         pnext[i] = pnext[i-1]+1
    #     elif
    """生成针对p中各位置i的下一检查位置表,用于KMP算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m  # 初始数组元素全为-1
    while i < m - 1:  # 生成下一个pnext元素值
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k  # 设置pnext元素
        else:
            k = pnext[k]  # 退到更短相同前缀
    return pnext


# pnext生成算法的改进:pi!=tj时,pnext[i]=k,如果pi=pk,那么pk!=tj.设pnext[i]=k,如果pi=pk,那么pk!=tj.
# 实际上模式串应该右移到pnext[k](而不是仅右移到pnext[i]),下一步应该用ppnext[k]与tj比较
def gen_pnext_p(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


if __name__ == '__main__':
    print(gen_pnext("abbcabcaabbcaa"))
    print(gen_pnext_p("abbcabcaabbcaa"))
