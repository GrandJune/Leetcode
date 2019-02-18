# -*- coding: utf-8 -*-
# @Time     : 2019/2/18 16:00
# @Author   : Junee
# @FileName: 53最大子序列和.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 经典算法题目
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = 0
        max_sub_sum = max(nums)
        for num in nums:
            sum_ += num
            if sum_ > max_sub_sum:
                max_sub_sum = sum_
                print(max_sub_sum)
            if sum_ < 0:
                sum_ = 0
        return max_sub_sum