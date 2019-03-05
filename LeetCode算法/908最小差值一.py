# -*- coding: utf-8 -*-
# @Time     : 2019/3/5 22:12
# @Author   : Junee
# @FileName: 908最小差值一.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if max(A) - min(A) > 2*K:
            return max(A) - min(A) -2*K
        else:
            return 0