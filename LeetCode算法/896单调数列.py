# -*- coding: utf-8 -*-
# @Time     : 2019/1/16 14:12
# @Author   : Junee
# @FileName: 896单调数列.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 我的解法
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 1:
            return True
        temp = [A[i+1]-A[i] for i in range(len(A)-1)]
        if (min(temp) >= 0) | (max(temp) <= 0):
            return True
        else:
            return False

# 一行代码版本
return A == sorted(A) or A[::-1] == sorted(A)