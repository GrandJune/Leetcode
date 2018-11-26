# -*- coding: utf-8 -*-
# @Time     : 2018/11/26 20:23
# @Author   : Junee
# @FileName: 排序算法.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import numpy as np
import time
# 选择排序
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i   # 初始化最小数的索引是每次循环的第一个数
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index],arr[i]  # 这行代码并无法实现互换
        # print('Round ',i,":",arr)
    return arr


test_arr = np.random.randint(1,10000,size=50)
print(test_arr)
# test_arr = [9891,9863,5139,9748,3785,6943,782,8288,99]
t0 = time.clock()
result = selection_sort(test_arr)
t1 = time.clock()
print("排序后数组：",result,"用时：",t1-t0)


t2 = time.clock()
test_arr_2 = np.random.randint(1,10000,size=50)
test_arr_2.sort()
t3 = time.clock()
print('自带的sort()函数结果：',test_arr_2,"用时",t3-t2)

# 结果表明列表自带的sort()方法要比选择排序快500倍,大数据量下。
# 数据量少的时候差距没那么大，但是还是sort()方法速度快

# 列表元素的互换
# test_list = [1,2,3,4]
# test_list[0],test_list[1] = test_list[1],test_list[0]
# print(test_list)