# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/5 20:17
# @Author   : tangky
# @Site     : 
# @File     : dlist.py
# @Software : PyCharm

from linklist import LNode, LinkedListUnderflow
from llist1 import LList1


class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


class DLList(LList1):  # 双链表类
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:  # 空表
            self._rear = p
        else:  # 非空表,设置prev引用
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:  # 空表插入
            self._head = p
        else:  # 非空表,设置next引用
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:  # _head空时不需要做任何事
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None  # 设置_head保证is_empty正确工作
        else:
            self._rear.next = None
        return e
