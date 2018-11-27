# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 16:17
# @Author   : Junee
# @FileName: 冒泡排序.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import time
import numpy as np
# 算法步骤
# 每次比较相邻的两个元素，把大的元素放右边；
# 每次循环都把这一趟最大的数放到最右边
# 所以有序的顺序会从右边逐渐累积到左边，完成排序
def bubble_sort(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
test_arr = np.random.randint(1,10000,size=10)
print(test_arr)
# test_arr = [9891,9863,5139,9748,3785,6943,782,8288,99]
t0 = time.clock()
result = bubble_sort(test_arr)
t1 = time.clock()
print("排序后数组：",result,"用时：",t1-t0)


t2 = time.clock()
test_arr_2 = np.random.randint(1,10000,size=10)
test_arr_2.sort()
t3 = time.clock()
print('自带的sort()函数结果：',test_arr_2,"用时",t3-t2)

# 大数据的量下，sort()算法要快10^4倍，差距非常大
# 数据量少的时候两者速度相差不大