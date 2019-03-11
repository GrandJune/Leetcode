# -*- coding: utf-8 -*-
# @Time     : 2019/3/11 11:15
# @Author   : Junee
# @FileName: 784字母大小写全排列.py
# @Software  : PyCharm
# Observing PEP 8 coding style

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S: return [S]
        rest = self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]