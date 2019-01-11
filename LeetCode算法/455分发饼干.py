# -*- coding: utf-8 -*-
# @Time     : 2019/1/11 14:32
# @Author   : Junee
# @FileName: 455分发饼干.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        for each in s:
            for child in g:
                if each >= child:
                    count += 1
                    g.remove(child)
                    break
        return count

def findContentChildren(self, g, s):
    # 使用指针方法，可以不用再remove()
    g = sorted(g)
    s = sorted(s)
    res = 0
    i , j = 0 , 0
    l1 , l2 = len(g) , len(s)
    while i < l1 and j<l2:
        if s[j] >= g[i]:
            res += 1
            i += 1
        j += 1

    return res