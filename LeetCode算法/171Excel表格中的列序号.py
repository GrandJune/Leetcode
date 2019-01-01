# -*- coding: utf-8 -*-
# @Time     : 2019/1/1 19:42
# @Author   : Junee
# @FileName: 171Excel表格中的列序号.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 字符转assic码
# a = ord('A') - 64
# print(a)
# 本质上是26进制和10进制的转换
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1:
            return ord(s) - 64
        res = 0
        for i in range(n):
            index = n - 1 - i
            val = s[i]
            res += 26 ** index * (ord(val) - 64)
        return res