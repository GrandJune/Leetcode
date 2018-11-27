# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 19:21
# @Author   : Junee
# @FileName: 希尔排序.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import time
import numpy as np
import math
# 希尔排序
# 算法步骤
#
def shell_sort(arr):
    gap = 1
    while (gap < len(arr)/3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

test_arr = np.random.randint(1,10000,size=5000)
print(test_arr)
# test_arr = [9891,9863,5139,9748,3785,6943,782,8288,99]
t0 = time.clock()
result = shell_sort(test_arr)
t1 = time.clock()
print("排序后数组：",result,"用时：",t1-t0)


t2 = time.clock()
test_arr_2 = np.random.randint(1,10000,size=5000)
test_arr_2.sort()
t3 = time.clock()
print('自带的sort()函数结果：',test_arr_2,"用时",t3-t2)

# 结果表明列表自带的sort()方法要比选择排序快100倍,大数据量下。
# 数据量少l两者算法在一个数量级上，但是还是sort()快一些