# -*- coding: utf-8 -*-
# @Time     : 2019/1/20 21:15
# @Author   : Junee
# @FileName: 263丑数.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        if num in [2,3,5]:
            return True
        else:
            if num % 2 == 0:
                return self.isUgly(num/2)
            elif num % 3 ==0:
                return self.isUgly(num/3)
            elif num % 5 == 0:
                return self.isUgly(num/5)
            else:
                return False