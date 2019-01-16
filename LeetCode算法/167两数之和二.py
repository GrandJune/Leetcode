# -*- coding: utf-8 -*-
# @Time     : 2019/1/16 15:20
# @Author   : Junee
# @FileName: 167两数之和二.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 第一版，费时间
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)-1):
            temp = numbers[i+1::]
            if (target-numbers[i]) in temp:
                return [i+1,temp.index(target-numbers[i])+i+2] #index会取到第一个
# 第二版，用哈希表进行加速
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(numbers)):
            if target-numbers[i] not in temp.keys():
                temp[numbers[i]] = i+1
            else:
                return [temp[target-numbers[i]],i+1]

# 第三版，使用迭代器，同时生成索引和取值，进一步加速
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,num in enumerate(numbers):
            if num in d:
                return [d[num],i+1]
            else:
                d[target-num]=i+1
