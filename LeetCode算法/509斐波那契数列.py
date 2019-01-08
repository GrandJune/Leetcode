# -*- coding: utf-8 -*-
# @Time     : 2019/1/8 20:46
# @Author   : Junee
# @FileName: 509斐波那契数列.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 递归入门
# 怎么把递归的每次结果累加起来是需要思考的问题
# return f(N-1)有可能只返回到最底层的那个数，而累加怎么办呢
# def fib(N):
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1
#     else:
#         return fib(N-1)
# res = fib(3)
# print(res)
# 像这种就是只返回了最底层的结果，不存在累加的过程
# 原题
def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fib(N-1) + fib(N-2)
res = fib(5)
print(res)