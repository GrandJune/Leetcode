# -*- coding: utf-8 -*-
# @Time     : 2018/8/11 20:42
# @Author   : Junee
# @FileName: 股票最大收益.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_ = 0
    min_ = float("Inf")
    len_ = len(prices)
    profit_list = [ 0 ]
    if len == 0:
        return 0
    elif len == 1:
        return 0
    else:
        for i in range(0, len_):
            print("-------")
            min_ = min(prices[ i ], min_)
            print("min: %d" % min_)
            for j in range(i + 1, len_):
                max_ = max(prices[ j ], max_)

            print("max: %d" % max_)
            profit = max_ - min_
            max_ = 0
            profit_list.append(profit)
            print(profit_list)
            print("-------")

        profit_list.sort()
        max_profit = profit_list.pop()
        if max_profit > 0:
            return max_profit
        else:
            return 0

m = maxProfit([7,6,5,4,2])
print(m)