#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午1８:26
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.８.py
# @Software: PyCharm

import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        s = ''
        while n > 0:
            s = str(n % 2) + s
            n = n / 2
        print(s)
    else:
        print("参数错误：请输入1个int参数")
        print("切到当前工作目录")
        print("cd /Users/siyu/Desktop/workSpace/Algorithms/ChapterOne")
        print("example: python 1.1.9.py  6")
