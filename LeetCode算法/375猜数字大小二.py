# -*- coding: utf-8 -*-
# @Time     : 2019/2/21 14:26
# @Author   : Junee
# @FileName: 375猜数字大小二.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for i in range(n+1)]
        for left in range(n-1, 0, -1):
            for right in range(left+1, n+1, 1):
                dp[left][right] = min( [ i+max(dp[left][i-1], dp[i+1][right]) for i in range(left, right)])
        return dp[1][n]