# -*- coding: utf-8 -*-
# @Time     : 2018/12/26 23:15
# @Author   : Junee
# @FileName: 最长特殊序列.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        len_a = len(a)
        len_b = len(b)
        if (len_a == 0) and (len_b==0):
            return -1
        elif a == b:
            return -1
        else:
            return max(len(a),len(b))