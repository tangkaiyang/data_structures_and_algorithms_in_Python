# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/8 19:29
# @Author   : tangky
# @Site     : 
# @File     : naive_match.py
# @Software : PyCharm


# 朴素匹配算法:两个局部函数:处理从模式中某个位置开始的匹配和模式中的星号
def match(re, text):
    def match_here(re, i, text, j):
        """检查从text[j]开始的正文是否与re[i]开始的模式匹配"""
        while True:
            if i == rlen:
                return True
            if re[i] == '$':
                return i + 1 == rlen and j == tlen
            if i + 1 < rlen and re[i + 1] == '*':
                return match_star(re[i], re, i + 2, text, j)
            if j == tlen or (re[i] != '.' and re[i] != text[j]):
                return False
            i, j = i + 1, j + 1

    def match_star(c, re, i, text, j):
        """在text里跳过0个或多个c后检查匹配"""
        for n in range(j, tlen):
            if match_here(re, i, text, n):
                return True
            if text[n] != c and c != '.':
                break
        return False

    rlen, tlen = len(re), len(text)

    if re[0] == '^':
        if match_here(re, 1, text, 0):
            return 1
    for n in range(tlen):
        if match_here(re, 0, text, n):
            return n
    return -1


if __name__ == '__main__':
    re = '^p*'
    text = 'appp'
    print(match(re, text))
