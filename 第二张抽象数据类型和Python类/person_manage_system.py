# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/5/2 20:56
# @Author   : tangky
# @Site     : 
# @File     : person_manage_system.py
# @Software : PyCharm
import datetime


class PersonValueError(ValueError):
    pass


class PersonTypeError(TypeError):
    pass


class Person:
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and
                sex in ("女", "男")):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)  # 生成一个日期对象
        except:
            raise PersonValueError("Wrong date:", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return datetime.date.today().year - self._birthday.year

    def set_name(self, name):  # 修改名字
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return " ".join((self._id, self._name,
                         self._sex, str(self._birthday)))

    def details(self):
        return ", ".join(("编号: " + self._id,
                          "姓名: " + self._name,
                          "性别: " + self._sex,
                          "出生日期: " + str(self._birthday)))


if __name__ == '__main__':
    p1 = Person("谢雨洁", "女", (1995, 7, 30), "1201510111")
    p2 = Person("汪力强", "男", (1990, 2, 17), "1201380324")
    p3 = Person("张子玉", "女", (1974, 10, 16), "0197401032")
    p4 = Person("李国栋", "男", (1962, 5, 24), "0196212018")

    plist2 = [p1, p2, p3, p4]
    for p in plist2:
        print(p)
    print("\nAfter sorting:")
    plist2.sort() # 使用了"小于"运算符
    for p in plist2:
        print(p.details())
    print("People created:", Person.num(), "\n")