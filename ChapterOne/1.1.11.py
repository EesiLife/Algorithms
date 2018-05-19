#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 上午2:10
# @Author  : EesiLife
# @Site    : https://github.com/EesiLife/
# @File    : 1.1.11.py
# @Software: PyCharm

import numpy as np
import random


def _get_random_num():
    return random.randrange(0, 2)


if __name__ == '__main__':

    # 创建3*3维数组
    b = np.array([[_get_random_num(), _get_random_num(), _get_random_num()],
                  [_get_random_num(), _get_random_num(), _get_random_num()],
                  [_get_random_num(), _get_random_num(), _get_random_num()]], dtype=bool)
    print(b)
    for i in range(0, len(b)+1):
        s = ''
        for j in range(0, len(b[0])+1):
            # print(str(i) + " + " + str(j))
            if i == 0 and j == 0:
                s += '  '
            elif i == 0:
                s += str(j) + ' '
            elif j == 0:
                s += str(i) + ' '
            else:
                if b[i-1, j-1]:
                    s += '* '
                else:
                    s += '  '
        print(s)

