#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 上午2:06
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.5.py
# @Software: PyCharm

# **********************************************************
# 编写一段程序，如果double类型的变量x和y都严格位于0和1之间则打印true
# 否则打印false
# ***********************************************************

import sys


def compare(x, y):
    if (x>0 and x<1 and y>0 and y<1):
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    if (len(sys.argv) > 2):
        compare(float(sys.argv[1]), float(sys.argv[2]))
    else:
        print("参数错误：请输入2个double参数")
        print("切到当前工作目录")
        print("cd /Users/siyu/Desktop/workSpace/Algorithms/ChapterOne")
        print("example: python 1.1.5.py  0.44 0.5")
        print("example: python 1.1.3.py  21 22")
