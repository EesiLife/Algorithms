#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 下午2:53
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.12.py
# @Software: PyCharm

if __name__ == '__main__':
    a = [9-i for i in range(10)]
    a = [a[a[i]] for i in range(10)]
    print(a)

