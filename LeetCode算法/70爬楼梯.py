# -*- coding: utf-8 -*-
# @Time     : 2019/1/22 17:12
# @Author   : Junee
# @FileName: 70爬楼梯.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 单纯使用递归会超时
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if n == 0:
        #     return 0
        # if n == 3:
        #     return 3
        # return self.climbStairs(n-2) + self.climbStairs(n-1)
        if n <= 2:
            return n
        s = [ 1, 2 ]
        for i in range(2, n):
            s.append(s[ i - 1 ] + s[ i - 2 ])
        return s[ n - 1 ]