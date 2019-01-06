# -*- coding: utf-8 -*-
# @Time     : 2019/1/6 14:23
# @Author   : Junee
# @FileName: 27移除元素.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         n = nums.pop(i)
        #         nums.append(n)
        #         count += 1
        #     if i == len(nums):
        #         break
        # for j in range(count-1):
        #     nums.pop()
        # return len(nums)

        j = len(nums)
        for i in range(j - 1, -1, -1):
            if nums[ i ] == val:
                nums.pop(i)
        return len(nums)