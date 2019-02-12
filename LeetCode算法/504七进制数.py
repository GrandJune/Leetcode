# -*- coding: utf-8 -*-
# @Time     : 2019/2/12 21:32
# @Author   : Junee
# @FileName: 504七进制数.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        temp = abs(num)
        res = ''
        while temp:
            i = temp % 7
            res += str(i)
            temp //= 7
        res = res[::-1]
        if num == 0:
            return '0'
        elif num > 0:
            return res
        else:
            return '-' + res