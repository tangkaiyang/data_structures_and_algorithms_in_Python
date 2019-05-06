# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/6 7:50
# @Author   : tangky
# @Site     : 
# @File     : josephus.py
# @Software : PyCharm


def josephus_A(n, k, m):
    people = list(range(1, n+1))

    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i+1) % n
        if num < n-1:
            print(', ', end="")
        else:
            print("")
    return


if __name__ == '__main__':
    josephus_A(10, 2, 7)

