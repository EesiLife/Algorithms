#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 上午1:12
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.3.py
# @Software: PyCharm

import sys

# *************
# 编写一个程序，从命令行得到三个整数参数。
# 如果他们头相等则打印equal, 否则打印 not equal


def compare(a, b, c):
    if( a==b and b==c):
        print("equal")
    else:
        print("not equal")


if __name__ == '__main__':
    if (len(sys.argv) > 3):
        compare(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        print("参数错误：请输入3个整数参数")
        print("切到当前工作目录")
        print("cd /Users/siyu/Desktop/workSpace/Algorithms/ChapterOne")
        print("example: python 1.1.3.py  3 3 3")
        print("example: python 1.1.3.py  2 3 3")
