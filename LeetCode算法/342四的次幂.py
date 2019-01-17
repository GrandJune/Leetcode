# -*- coding: utf-8 -*-
# @Time     : 2019/1/17 21:38
# @Author   : Junee
# @FileName: 342四的次幂.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num < 4:
            return False
        if num % 4 != 0:
            return False
        return self.isPowerOfFour(num/4)
