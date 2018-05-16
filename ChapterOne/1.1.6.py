#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 上午2:21
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.6.py
# @Software: PyCharm

# **********************************************************
# 下面这段程序会打印出什么？
# int f = 0;
# int g = 1;
# for (int i = 0; i <= 15; i++){
#     StdOut.println(f)
#     f = f + g;
#     g = f - g;
# }
# 否则打印false
# ***********************************************************


# out **********************************************
# 0
# 1
# 1
# 2
#
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377



if __name__ == '__main__':
    f = 0
    g = 1
    for i in range(0, 15):
        print(f)
        f = f + g
        g = f - g