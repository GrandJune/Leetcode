# -*- coding: utf-8 -*-
# @Time     : 2019/3/21 23:43
# @Author   : Junee
# @FileName: 561数组拆分.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(len(nums)):
            if i %2 ==0:
                res+=nums[i]
        return(res )