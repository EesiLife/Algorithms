#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 下午3:15
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.13.py
# @Software: PyCharm

import random
import sys


def _generate_matrix(m, n):
    return [[random.randint(0, 10) for i in range(n)] for j in range(m)]


def _reverse_matrix(arr):
    print([[r[col] for r in arr] for col in range(len(arr[0]))])


if __name__ == '__main__':
    if len(sys.argv) > 2:
        M = int(sys.argv[1])
        N = int(sys.argv[2])
        print('M={}, N={}'.format(M, N))
        m1 = _generate_matrix(M, N)
        print(m1)
        _reverse_matrix(m1)
    else:
        print("参数错误：请输入2个int参数")
        print("切到当前工作目录")
        print("cd /Users/siyu/Desktop/workSpace/Algorithms/ChapterOne")
        print("example: python 1.1.13.py 3 4")