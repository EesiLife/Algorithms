#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 下午11:41
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.20.py
# @Software: PyCharm

import math


def __getN(n):
    m = 0
    for i in range(n):
        m *= (i+1)
    return m


def _getln_e(a):
    b = 0
    c = float(0)
    d = 0
    while a > 0:
        if(d == 0):
            c = float(a)/math.e
