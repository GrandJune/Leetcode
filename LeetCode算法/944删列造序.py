# -*- coding: utf-8 -*-
# @Time     : 2019/3/18 23:55
# @Author   : Junee
# @FileName: 944删列造序.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution:
    def minDeletionSize(self, A):

        if not len(A):
            return 0
        res = 0
        for num in range(len(A[0])):
            new_list = [x[num] for x in A]
            if not new_list == sorted(new_list):
                res += 1

        return res