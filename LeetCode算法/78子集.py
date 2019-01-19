# -*- coding: utf-8 -*-
# @Time     : 2019/1/19 21:35
# @Author   : Junee
# @FileName: 78子集.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import copy

class Solution:
    def recursive(self, nums, ret=[ ], pre=[ ], s=0):
        if s == len(nums) - 1:
            pre.append(nums[ s ])
            ret.append(copy.copy(pre))
            pre.pop()
            return ret
        for i in range(s, len(nums)):
            pre.append(nums[ i ])
            ret.append(copy.copy(pre))
            self.recursive(nums, ret, pre, i + 1)
            pre.pop()
        return ret

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = [ [ ] ]
        return self.recursive(nums, ret)