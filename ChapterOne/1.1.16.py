#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 上午12:50
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.16.py
# @Software: PyCharm


def __exR1__(n):
    if n <= 0:
        return ''
    else:
        return __exR1__(n-3) + str(n) + __exR1__(n-2) + str(n)


if __name__ == '__main__':
    print(__exR1__(6))