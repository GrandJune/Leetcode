# -*- coding: utf-8 -*-
# @Time     : 2019/1/8 22:05
# @Author   : Junee
# @FileName: 389找不同.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 抵消重复内容，转化为二进制取差值（因为只有一个不同）
        # sum_s,sum_t = 0,0
        # for each in s:
        #     sum_s += ord(each)
        # for each in t:
        #     sum_t += ord(each)
        # return chr(sum_t - sum_s)

        # 使用异或操作
        res = 0
        for each in s:
            res ^= ord(each)
        for each in t:
            res ^= ord(each)
        return chr(res)