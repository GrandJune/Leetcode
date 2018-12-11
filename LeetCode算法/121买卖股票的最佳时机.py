# -*- coding: utf-8 -*-
# @Time     : 2018/12/11 10:57
# @Author   : Junee
# @FileName: 121买卖股票的最佳时机.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# 一次遍历，维护一个最小值，和最大收益
class Solution:
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_p = len(prices)
        if len_p == 0:
            return 0
        min_price,max_gain = prices[0],0
        for each in prices:
            if each < min_price:
                min_price = each
            elif (each - min_price > max_gain):
                max_gain = each - min_price
        return max_gain