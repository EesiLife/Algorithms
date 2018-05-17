#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 上午1:26
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.7.py
# @Software: PyCharm

if __name__== '__main__':
    ## a
    t = 9.0
    while ( abs(t - 9.0/t ) > .001):
        t = (9.0/t + t) /2.0
    print(t)
    ## b
    sum = 0
    for i in range(1, 1000):
        for j in range(0, i):
            sum += 1
    print(sum)
    ## c
    sum = 0
    i = 1
    while i < 1000:
        for j in range(0, 1000):
            sum += 1
        i *= 2
    print(sum)

