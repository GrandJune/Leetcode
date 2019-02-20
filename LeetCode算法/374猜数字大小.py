# -*- coding: utf-8 -*-
# @Time     : 2019/2/20 14:21
# @Author   : Junee
# @FileName: 374猜数字大小.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# class Solution(object):
#     def guessNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return self.help(1,n)
#     def help(self,s,e):
#             m = (s + e) // 2
#             res = guess(m)
#             if res == 1:
#                 return self.help(s,m-1)
#             elif res == -1:
#                 return self.help(m+1,e)
#             else:
#                 return m
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=0
        right=n
        while left<=right:
            middle=(left+right)//2
            num=guess(middle)
            if num==-1:
                right=middle-1
            elif num==0:
                return middle
            else:
                left=middle+1
