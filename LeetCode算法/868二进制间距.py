# -*- coding: utf-8 -*-
# @Time     : 2019/1/9 15:24
# @Author   : Junee
# @FileName: 868二进制间距.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = list(str(bin(N)))
        temp = []
        for i in range(len(N)):
            if N[i] == '1':
                temp.append(i)
        if len(temp) < 2:
            return 0
        else:
            res = [temp[i+1]-temp[i] for i in range(len(temp)-1)]
            return max(res)