# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/5 19:39
# @Author   : tangky
# @Site     : 
# @File     : lclist.py
# @Software : PyCharm

from linklist import LNode, LinkedListUnderflow


class LCList:  # 循环单链表类
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 前端插入
        p = LNode(elem)
        if self._rear is None:
            p.next = p  # 建立一个结点的环
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):  # 尾端插入
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):  # 前端弹出
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop_last of CLList")
        r = self._rear.elem
        p = self._rear.next
        while p.next is not self._rear:
            p = p.next
        e = self._rear.next
        self._rear = p
        p.next = e
        return r

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next


if __name__ == '__main__':
    # llist1 = LNode(1)
    # p = llist1
    # for i in range(2, 11):
    #     p.next = LNode(i)
    #     p = p.next
    # p = llist1
    # print(p)
    # while p is not None:
    #     print(p.elem)
    #     p = p.next
    mlist1 = LCList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()
    print(mlist1.pop_last())
    mlist1.printall()
