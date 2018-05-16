#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 上午1:08
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.1_1.1.2.py
# @Software: PyCharm


def run():
    print("1.1  给出一下表达式的值")
    print("a. (0 + 15) / 2 = " + str((0 + 15) /2))
    print("b. 2.0e-6 * 100000000.1 = " + str(2.0e-6 * 100000000.1))
    print("c. true && false || true && false = " + str(True and False or True and False))
    print("*******************")
    print("1.2  给出一下表达式的值")
    print("a. 1 + 2.236/2 = " + str(1 + 2.236/2) + " type: " + str(type(1 + 2.236/2)))
    print("b. 1 + 2 + 3 + 4.0 = " + str(1 + 2 + 3 + 4.0) + " type: " + str(type(1 + 2 + 3 + 4.0)))
    print("c. 4.1 >= 4 = " + str(4.1 >= 4) + " type: " + str(type(4.1 >= 4)))
    print("d. 1 +2 + \"3\" = " + str(str(1 + 2) + "3") + " type: " + str(type(str(1 + 2) + "3")))


if __name__ == '__main__':
    run()
