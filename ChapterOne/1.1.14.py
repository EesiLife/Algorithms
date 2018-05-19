#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 上午12:08
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.14.py
# @Software: PyCharm

import sys


def __log2N(n):
    i = -1
    while n > 0:
        print(n)
        n = int(n/2)
        i += 1
    return i


if __name__ == '__main__':
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
        print('不大于log2 {}的最大整数为{}'.format(N, __log2N(int(sys.argv[1]))))
    else:
        print("参数错误：请输入1个int参数")
        print("切到当前工作目录")
        print("cd /Users/siyu/Desktop/workSpace/Algorithms/ChapterOne")
        print("example: python 1.1.14.py 3")
