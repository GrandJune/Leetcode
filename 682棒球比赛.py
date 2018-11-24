# -*- coding: utf-8 -*-
# @Time     : 2018/11/24 22:22
# @Author   : Junee
# @FileName: 682棒球比赛.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# 栈，其实在Python 里头就是一个列表，列表可以做数组，可以做栈
# 堆则需要用到heapq包
class Solution(object):
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)