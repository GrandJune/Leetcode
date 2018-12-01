# -*- coding: utf-8 -*-
# @Time     : 2018/12/1 22:25
# @Author   : Junee
# @FileName: 递归图搜索.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 一道面试算法题，大致如下：给定n<=2，给出跳n步的所有可能路线数量，每次只能跳上左右，不能重复踩点，即不能回跳

# print(count)

def find(last_move='None',n=1):
    if n == 1:
        if (last_move == '上') | (last_move == 'None'):
            return 3
        else:
            return 2
    else:
        if (last_move == "上") | (last_move == 'None'):
            return find('左',n-1) + find('右',n-1) + find('上',n-1)
        elif last_move == '左':
            return find('上',n-1) + find('右', n-1)
        elif last_move == '右':
            return find('上',n-1) + find('左', n-1)
        # elif last_move == 'None':
        #     return find('上', n-1) + find('左', n-1) + find('右', n-1)
import time
t0 = time.clock()
result = find(n=10)
t1 = time.clock()
print(result,t1-t0)
