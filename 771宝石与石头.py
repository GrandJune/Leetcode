# -*- coding: utf-8 -*-
# @Time     : 2018/11/25 23:42
# @Author   : Junee
# @FileName: 771宝石与石头.py
# @Software  : PyCharm
# Observing PEP 8 coding style

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jlist = list(J)
        slist = list(S)
        all = 0
        for each in slist:
            if each in jlist:
                all += 1
        return all