# -*- coding: utf-8 -*-
# @Time     : 2019/2/17 22:46
# @Author   : Junee
# @FileName: 970强整数.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def powerfulIntegers(x, y, bound):
    """
    :type x: int
    :type y: int
    :type bound: int
    :rtype: List[int]
    """
    max_ = max(x,y)
    min_ = min(x,y)
    def help(x,y,i,j):
        return (x^i+y^i)
    res = []
    i,j = 0,0
    while True:
        temp = help(max_,min_,i,j)
        if temp <= bound:
            res.append(temp)
            if i == j :
                j += 1
            else:
                i += 1
        else:
            return res
res = powerfulIntegers(2,3,10)
print(3**0 + 2**0)
# print(res)
# 第一种写法，按照先升小数的幂，再升大数的幂，存在错误，比如:
# 2的三次方+3的零次方这种相差两次幂的
# 暴力解法
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        min_ = min(x, y)
        power_range = 0
        for i in range(bound):
            power_range = i
            if min_ ** power_range > bound:
                break
        for i in range(power_range):
            for j in range(power_range):
                if x ** i + y ** j <= bound:
                    if (x ** i + y ** j) not in res:
                        res.append( x ** i + y ** j)
        return (res)