# -*- coding: utf-8 -*-
# @Time     : 2019/1/8 20:30
# @Author   : Junee
# @FileName: 412FizzBuzz.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 简单的条件语句写法
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 ==0 :
                result.append('FizzBuzz')
            elif i % 3 == 0 :
                result.append('Fizz')
            elif i % 5 ==0 :
                result.append('Buzz')
            else :
                result.append(str(i))
        return result