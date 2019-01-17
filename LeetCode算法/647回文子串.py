# -*- coding: utf-8 -*-
# @Time     : 2019/1/17 17:35
# @Author   : Junee
# @FileName: 647回文子串.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = list(s)
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         temp = s[j::]
        #         if temp == temp[::-1]:
        #             count += 1
        #             print(temp)
        # return count
    # 这种情况没法取到中间相邻的两个相同字符，如hello中的ll
    # 此处要用到动态规划的思想
        n=len(s)
        count=0
        for i in range(0,n-1):
            left=i-1
            right=i+1
            # 奇数长度的回文子串
            while left>=0 and right<n:
                if s[left]==s[right]:
                    count+=1
                    left-=1
                    right+=1
                else:
                    break
            # 偶数长度的回文子串
            left=i
            right=i+1
            while left>=0 and right<n:
                if s[left]==s[right]:
                    count+=1
                    left-=1
                    right+=1
                else:
                    break
        return count+n
