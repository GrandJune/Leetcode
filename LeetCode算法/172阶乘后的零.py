# -*- coding: utf-8 -*-
# @Time     : 2019/1/22 16:21
# @Author   : Junee
# @FileName: 172阶乘后的零.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        while 5**i<n:
            i+=1
        num=0
        while i!=0:
            num+=n//(5**i)
            i-=1
        return num