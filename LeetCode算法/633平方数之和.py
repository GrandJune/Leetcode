# -*- coding: utf-8 -*-
# @Time     : 2019/2/22 19:57
# @Author   : Junee
# @FileName: 633平方数之和.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            total = i * i + j * j
            if total > c:
                j = j - 1
            elif total < c:
                i = i + 1
            else:
                return True
        return False