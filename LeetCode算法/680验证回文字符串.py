# -*- coding: utf-8 -*-
# @Time     : 2019/2/25 22:18
# @Author   : Junee
# @FileName: 680验证回文字符串.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 很巧妙的解法，第一点：遍历时候很多考虑遍历到一半，或者遍历到平方根；
# 因为只限制一次出错，所以巧妙的用了列表的切片和列表的转置的写法，很漂亮
# 列表的转置list.reverse(),或者list[::-1]，注意第一种返回的是None
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i = 0
        while i < n // 2 and s[i] == s[-(i+1)]:
            i += 1
        temp = s[i:n-i]
        return temp[1:] == temp[1:][::-1] or temp[:-1] == temp[:-1][::-1


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        i = 0
        j = len(s) - 1
        # 此处的i<j实际上也是限制了ij到达中点处
        while i < j:
            if s[i] != s[j]:
                return s[i:j]==s[i:j][::-1] or s[i+1:j+1][::-1] == s[i+1:j+1]
            i,j = i+1, j-1