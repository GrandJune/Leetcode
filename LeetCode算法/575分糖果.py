# -*- coding: utf-8 -*-
# @Time     : 2019/1/8 20:20
# @Author   : Junee
# @FileName: 575分糖果.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 集合的应用，把一个字典转化为没有重复元素的集合
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)),len(candies)/2)