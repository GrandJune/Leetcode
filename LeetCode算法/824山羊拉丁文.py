# -*- coding: utf-8 -*-
# @Time     : 2019/3/3 12:33
# @Author   : Junee
# @FileName: 824山羊拉丁文.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        suffix = 'a'
        yuan = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = ""
        for word in S.split(" "):
            if word[0] not in yuan:
                word = word[1:] + word[0]
            word = word + "ma" + suffix
            res = res + word + " "
            suffix = suffix + 'a'
        return res[0:-1]