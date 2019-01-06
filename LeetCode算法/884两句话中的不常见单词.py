# -*- coding: utf-8 -*-
# @Time     : 2019/1/6 14:00
# @Author   : Junee
# @FileName: 884两句话中的不常见单词.py
# @Software  : PyCharm
# Observing PEP 8 coding style
A = "this apple is sweet"
B = "this apple is sour"
a = A.split(' ')
print(a)
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        res = []
        A = A.split(' ')
        B = B.split(' ')
        temp_A = {}
        temp_B = {}
        for each in A:
            if each not in temp_A.keys():
                temp_A[each] = 1
            else:
                temp_A[each] += 1
        for each in B:
            if each not in temp_B.keys():
                temp_B[each] = 1
            else:
                temp_B[each] += 1
        for each in A:
            if (each not in B) and (temp_A[each] == 1):
                res.append(each)
        for each in B:
            if (each not in A) and (each not in res) and (temp_B[each] == 1):
                res.append(each)
        return res