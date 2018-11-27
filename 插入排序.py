# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 16:40
# @Author   : Junee
# @FileName: 插入排序.py
# @Software  : PyCharm
# Observing PEP 8 coding style

import time
import numpy as np

# 算法步骤
#
# 插入排序
def insertion_sort(arr):
    for i in range(len(arr)):
        pre_index = i - 1# 每次循环定索引为前一个位置
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index+1] = arr[pre_index]  # 把大的值往右边挪，
            # 第一次找到的时候，替换的是arr[i]，但是我们把a[i]的值保存在current中了，所以没关系，循环结束再把current值放到合适的位置
            pre_index -= 1  # 我们要找到当前这个current的合适位置，所以需要遍历
        arr[pre_index+1] = current # 找到那个合适的位置就把值赋上
    return arr

test_arr = np.random.randint(1,10000,size=50)
print(test_arr)
# test_arr = [9891,9863,5139,9748,3785,6943,782,8288,99]
t0 = time.clock()
result = insertion_sort(test_arr)
t1 = time.clock()
print("排序后数组：",result,"用时：",t1-t0)


t2 = time.clock()
test_arr_2 = np.random.randint(1,10000,size=50)
test_arr_2.sort()
t3 = time.clock()
print('自带的sort()函数结果：',test_arr_2,"用时",t3-t2)

# 结果表明列表自带的sort()方法要比选择排序快500倍,大数据量下。
# 数据量少的时候差距没那么大，但是还是sort()方法速度快