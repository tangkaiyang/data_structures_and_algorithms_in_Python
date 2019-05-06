# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/5 16:07
# @Author   : tangky
# @Site     : 
# @File     : linklist.py
# @Software : PyCharm


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:  # 无结点,引发异常
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    # 后端操作:在链表的最后插入元素,必须先找到链表的最后一个结点.其实现首先是一个扫描循环,找到相应结点后把包含新元素的结点插入在其后.
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # 这里需要区分两种情况:如果原表为空,引用新结点的就应该是表对象的_head域,否则就是已有的最后结点的next域
    # 删除表中最后的操作,删除最后的结点,需要处理两种特殊情况:如果表空没有可返回的元素时应该引发异常.表中只有一个
    # 元素的情况需要特殊处理,因为这是应该修改表头指针.一般情况是先通过循环找到位置,取出最后结点的数据后将其删除
    def pop_last(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:  # 知道p.next是最后结点
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    # 其他操作:
    # LList类的下一个方法是找到满足给定条件的表元素.这个方法有一个参数,调用时通过参数提供一个判断谓词,该方法
    # 返回第一个满足谓词的表元素.
    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    # 被操作表的当前情况
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')  # 为了输出一个换行符号

    # 为类定义对象的一个迭代器:
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    # 筛选生成器
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    # 链表反转
    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next  # 摘下原来的首结点
            q._next = p
            p = q  # 将刚摘下的结点加入p引用的结点序列
        self._head = p  # 反转后的结点序列已经做好,重置表头链接

    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next  # 从首结点之后开始处理
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:  # 跳过小元素
                p = p.next
            while p is not crt:  # 倒换大元素,完成元素插入的工作
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next  # 回填最后一个元素

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p


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
    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()
    for x in mlist1.elements():
        print(x)
