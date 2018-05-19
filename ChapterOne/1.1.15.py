#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 上午12:33
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.15.py
# @Software: PyCharm


def __histogram(a, M):
    arr = []
    for i in range(0, M):
        num = 0
        for j in range(0, len(a)):
            if i + 1 == a[j]:
                num += 1
        arr.append(num)
    return arr


if __name__ == '__main__':
    a = [1, 2, 2, 3, 4, 5, 6, 5, 5, 5, 4]
    M = 7
    print(__histogram(a, M))
