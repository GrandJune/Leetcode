# -*- coding: utf-8 -*-
# @Time     : 2019/2/23 21:56
# @Author   : Junee
# @FileName: 46全排列.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# itertools 迭代器模块
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        res = list(itertools.permutations(nums))
        # res = sorted(res,key=lambda x:x[0])
        # res.sort()
        return res

# 法二，迭代法，固定第一个数，对后面的数全排列，以此类推
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums,0)
        return self.res
    def helper(self,nums,i):
        nums1 = nums[:]
        if i == (len(nums1)-1):
            self.res.append(nums1)
            return
        # return与return None的效果相同，退出函数返回空值
        for l in range(i,len(nums)):
            nums1[i],nums1[l]=nums1[l],nums1[i]
            self.helper(nums1,i+1)
            nums1[i],nums1[l]=nums1[l],nums1[i]

# 法三：dfs深度优先搜索
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [ ]
        vis = [ ]

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[ : ])
                return

            for i in nums:
                if not i in vis:
                    vis.append(i)
                    path.append(i)
                    dfs(path)
                    path.pop()
                    vis.remove(i)
        dfs([ ])
        return res