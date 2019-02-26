# -*- coding: utf-8 -*-
# @Time     : 2019/2/26 19:10
# @Author   : Junee
# @FileName: 859亲密字符串.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        len_a = len(A)
        len_b = len(B)
        if len_a != len_b:
            return False
        if len_a == 0:
            return False
        temp = []
        for i in range(len_a):
            if A[i] != B[i]:
                temp.append(i)
        if len(temp) > 2:
            return False
        elif len(temp) == 2:
            m = temp[0]
            n = temp[1]
            if (A[m] == B[n]) and (A[n] == B[m]):
                return True
            else:
                return False
        elif len(temp) == 0:
            A_dict = {}
            for each in A:
                if each not in A_dict.keys():
                    A_dict[each] = 1
                else:
                    A_dict[each] += 1
            for each in A_dict.values():
                if each > 1:
                    return True
                else:
                    return False
        else:
            print(temp)
            return False