# -*- coding: utf-8 -*-
# @Time     : 2019/2/12 23:37
# @Author   : Junee
# @FileName: 28实现strStr().py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        len_h = len(haystack)
        len_n = len(needle)
        if len_h < len_n:
            return -1
        for i in range(len_h):
            if i + len_n < len_h:
                if haystack[i:i+len_n] == needle:
                    return i
            else:
                # 这个else是搜索到字符串末尾的情况：所以之前不能写return -1
                if haystack[i:i+len_n] == needle:
                    return i
                else:
                    return -1