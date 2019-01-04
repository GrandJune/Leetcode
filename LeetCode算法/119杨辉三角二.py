# -*- coding: utf-8 -*-
# @Time     : 2019/1/4 16:58
# @Author   : Junee
# @FileName: 119杨辉三角二.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 1:
            return [1,1]
        res = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            temp = [res[i-1][j] + res[i-1][j+1] for j in range(len(res[i-1])-1)]
            temp = [1] + temp + [1]
            res.append(temp)
        return res[rowIndex]