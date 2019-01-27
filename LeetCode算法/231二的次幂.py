# -*- coding: utf-8 -*-
# @Time     : 2019/1/27 21:16
# @Author   : Junee
# @FileName: 231二的次幂.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if (n & n-1) == 0:
            return True
        return False
# 一行代码
# return n > 0 and  (n & n-1) == 0