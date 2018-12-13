# -*- coding: utf-8 -*-
# @Time     : 2018/12/12 18:19
# @Author   : Junee
# @FileName: 123买卖股票的最佳时机三.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    current = prices[ 0 ]
    gain = 0
    gain_list = [ ]
    for each in prices:
        print('***',current)
        if each > current:
            gain += (each - current)
            if prices.index(each) == (len(prices) - 1):
                print("end")
                gain_list.append(gain)
        elif each < current:
            gain_list.append(gain)   # 这样写会漏掉一个情况，当序列结束时还是递增的时候，最后那个gain值没有被存下来
            gain = 0
        else:
            pass
        current = each
        print(gain_list)


    if len(gain_list) < 1:
        return 0
    elif len(gain_list) == 1:
        return gain_list[ 0 ]
    else:
        # print(gain_list)
        gain_list.sort()
        return gain_list[-1] + gain_list[-2]

def maxProfit_2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    current = prices[ 0 ]
    gain = 0
    gain_list = [ ]
    i = 0
    while i < len(prices):
        if prices[ i ] > current:
            gain += (prices[ i ] - current)

        elif prices[ i ] < current:
            gain_list.append(gain)
            gain = 0
        current = prices[ i ]
        i += 1

    gain_list.append(gain)
    if len(gain_list) == 1:
        return gain_list[ 0 ]
    elif len(gain_list) == 2:
        return gain_list[ 0 ] + gain_list[ 1 ]
    else:
        gain_list.sort()
        return gain_list[ -1 ] + gain_list[ -2 ]

# prices = [3,3,5,0,0,3,1,4]
# prices = [2,1,2,0,1]
# a = maxProfit_2(prices)
# print(a)

# for each in prices:
#     a = prices.index(each)
#     # 不能用这种写法取索引，当存在重复元素时，只取到最小的索引
#     print(a)

# 以上两种写法不适用与第三种最佳时机，一个错误的例子：[1,2,4,2,5,7,2,4,9,0]
# 这里由于有两次限制，导致了可能存在1-7,2-9这种长跨度的解，而我们这种短视角的写法没有找到这种大跨度的最优解
def maxProfit_3(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n == 0:
        return 0

    prices.append(0)
    i = 1
    sum_gain = 0
    while i < n:
        max_gain_1 = 0
        max_gain_2 = 0
        min_price = prices[0]
        for j in range(i+1):
            if prices[j] < min_price:
                min_price = prices[j]
            elif (prices[j] - min_price) > max_gain_1:
                max_gain_1 = prices[j] - min_price

        min_price_2 = prices[i+1]
        for k in range(i+1,n):
            if prices[k] < min_price_2:
                min_price_2 = prices[k]
            elif (prices[k] - min_price_2) > max_gain_2:
                max_gain_2 = (prices[k] - min_price_2)

        print(max_gain_1,max_gain_2,'***',i)
        sum_gain = max(max_gain_1+max_gain_2,sum_gain)
        i += 1
        return sum_gain
# prices = [1,2,4,2,5,7,2,4,9,0]
# prices = [2,1,4]
# a = maxProfit_3(prices)
# print(a)

def maxProfit_4(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n in [0,1]:
        return 0
    sum_gain = 0
    prices.append(0)
    print(prices)
    for i in range(1,n):
        if prices[i] > prices[i-1]:
            max_gain_1 = part_maxProfit(prices[:i+1])
            max_gain_2 = part_maxProfit(prices[i+1:])
            sum_gain = max(sum_gain,max_gain_2+max_gain_1)
        else:
            pass
    return sum_gain
def part_maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    len_p = len(prices)
    if len_p in [0,1]:
        return 0
    min_price, max_gain = prices[0], 0
    for each in prices:
        if each < min_price:
            min_price = each
        elif (each - min_price > max_gain):
            max_gain = each - min_price
    return max_gain

prices = [1,2,4,2,5,7,2,4,9,0]
# prices = [2,1,4]
a = maxProfit_4(prices)
print(a)