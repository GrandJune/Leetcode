# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 21:31
# @Author   : Junee
# @FileName: 1002查找常用字符.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# all()函数的使用，不常常使用都忘了，以及any()函数
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        for i in A[0]:
            if all(i in j for j in A[1:]):
                result.append(i)
            for x in range(1,len(A)):
                if i in A[x]:
                    index = A[x].find(i)
                    A[x] = A[x][:index]+A[x][index+1:]
        return result