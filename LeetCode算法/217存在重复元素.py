# -*- coding: utf-8 -*-
# @Time     : 2019/1/11 15:18
# @Author   : Junee
# @FileName: 217存在重复元素.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 超时
        # temp = {}
        # for each in nums:
        #     if each not in temp.keys():
        #         temp[each] = 1
        #     else:
        #         return True
        # return False

        #抑或操作，比较相邻元素即可
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                return True
        return False