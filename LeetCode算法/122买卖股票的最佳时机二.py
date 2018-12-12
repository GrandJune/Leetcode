# -*- coding: utf-8 -*-
# @Time     : 2018/12/12 18:00
# @Author   : Junee
# @FileName: 122买卖股票的最佳时机二.py
# @Software  : PyCharm
# Observing PEP 8 coding style

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        current = prices[0]
        gain = 0
        for each in prices:
            if each > current:
                gain += (each - current)   # 每一次取尽能套取的利润
            current = each
        return gain