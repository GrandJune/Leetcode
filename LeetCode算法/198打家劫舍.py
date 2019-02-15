# -*- coding: utf-8 -*-
# @Time     : 2019/2/15 15:46
# @Author   : Junee
# @FileName: 198打家劫舍.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = max(sum(nums[::2]),sum(nums[1::2]))
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        res = []
        res.append(nums[0])
        res.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            res.append(max(nums[i] + res[i-2],res[i-1]))
        return res[-1]