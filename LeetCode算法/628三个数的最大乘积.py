# -*- coding: utf-8 -*-
# @Time     : 2019/2/12 21:22
# @Author   : Junee
# @FileName: 628三个数的最大乘积.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
    # 只有两种情况：最大的三个整数乘积；最小的两个负数乘以最大的整数