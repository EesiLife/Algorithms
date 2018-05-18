#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午1８:26
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.８.py
# @Software: PyCharm

import sys
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
        s = ''
        while(n > 1):
            j = n % 2
            n = n / 2
            s += str(j)
            if (n == 1):
                s += str(1)
        print(s[::-1])
