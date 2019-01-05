# -*- coding: utf-8 -*-
# @Time     : 2019/1/5 19:56
# @Author   : Junee
# @FileName: 136只出现一次的数字.py
# @Software  : PyCharm
# Observing PEP 8 coding style
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 2
    for num in nums:
        a ^= num
        print(a)
    return a
# 抑或运算，将数字转换为对应的二进制码再进行二进制运算
nums = [1,2,1]
a = singleNumber(nums)
print('*****')
print(a)