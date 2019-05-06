# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/6 7:50
# @Author   : tangky
# @Site     : 
# @File     : josephus.py
# @Software : PyCharm


def josephus_A(n, k, m):
    people = list(range(1, n + 1))  # 构造一个有n个元素的list

    i = k - 1  # 从第k个元素开始
    for num in range(n):  # 循环取出people中的元素,进行n次循环
        count = 0  # 报数开始
        while count < m:  # 报到m止
            if people[i] > 0:  # 跳过空位即为0的元素
                count += 1
            if count == m:  # 报到m时取出元素
                print(people[i], end="")
                people[i] = 0  # 设为0,空位
            i = (i + 1) % n
        if num < n - 1:
            print(', ', end="")
        else:
            print("")
    return


def josephus_L(n, k, m):
    people = list(range(1, n+1))
    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i),
              end=(", " if num > 1 else "\n"))
    return


if __name__ == '__main__':
    josephus_A(10, 2, 7)
    josephus_L(10, 2, 7)
