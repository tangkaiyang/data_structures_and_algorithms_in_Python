# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/11 7:18
# @Author   : tangky
# @Site     : 
# @File     : check_parens.py
# @Software : PyCharm


class StackUnderflow(ValueError):
    pass


class SStack():  # 基于顺序表技术实现的栈类
    def __init__(self):  # 用list对象_elems存储栈中元素
        self._elems = []  # 所有栈操作都映射到list操作

    def is_empty(self):
        return self._elems == []

    def top(self):
        if not self._elems:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if not self._elems:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()


def check_parens(text):
    """括号配对检查函数,text是被检查的正文串"""
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}

    def parentheses(text):
        """括号生成器,每次调用返回text里的下一个括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()  # 保存括号的栈
    for pr, i in parentheses(text):  # 对text里各括号的位置迭代
        if pr in open_parens:  # 开括号,压进栈并继续
            st.push(pr)
        elif st.pop() != opposite[pr]:  # 不匹配就是失败,退出
            print('Unmatching is found at', i, 'for', pr)
            return False
        # else:这是一次括号配对成功,什么也不做,继续
    print("All parentheses are correctly matched.")
    return True


print(check_parens(r"{{}}{((())"))
