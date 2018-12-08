# -*- coding: utf-8 -*-
# @Time     : 2018/12/8 23:53
# @Author   : Junee
# @FileName: 467数字的部署.py
# @Software  : PyCharm
# Observing PEP 8 coding style
def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    s = 1
    while s <= num:
        s <<= 1
    return (s - 1) ^ num

b = findComplement(5)
print(b)