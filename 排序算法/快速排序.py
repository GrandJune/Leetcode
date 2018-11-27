# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 19:41
# @Author   : Junee
# @FileName: 快速排序.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import time
import numpy as np

# 快速排序
# 在平均情况下，排序n个项目需要O(nlogn)次比较，只有在最坏情况下才需要O(n2)
# 快速排序通常比其他O(nlogn)算法更快
# 快速排序使用分治法将一个列表分成两个子列表
# 从列表中选择一个元素作为基准，比基准小的放在左边，大的放在右边
# 递归地把两边的子列表进行排序


def quick_sort(arr,left=None,right=None):
    left = 0 if not isinstance(left,(int,float)) else left
    right = len(arr) - 1 if not isinstance(right,(int,float)) else right
    if left < right:
        partition_index = partition(arr,left,right)
        quick_sort(arr,left,partition_index-1)  # 对左边子列表进行排序
        quick_sort(arr,partition_index+1,right) # 对右边子列表进行排序
    return arr


def partition(arr,left,right):
    pivot = left    # 中心点pivot
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr,i,index)
            index += 1
        i += 1
    swap(arr,pivot,index-1)
    return index-1


def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


test_arr = np.random.randint(1,10000,size=50)
print(test_arr)
# test_arr = [9891,9863,5139,9748,3785,6943,782,8288,99]
t0 = time.clock()
result = quick_sort(test_arr)
t1 = time.clock()
print("排序后数组：",result,"用时：",t1-t0)


t2 = time.clock()
test_arr_2 = np.random.randint(1,10000,size=50)
test_arr_2.sort()
t3 = time.clock()
print('自带的sort()函数结果：',test_arr_2,"用时",t3-t2)

# 结果表明列表自带的sort()方法要比快速排序快100倍,大数据量下。
# 数据量少时，sort()方法要比快速排序快十倍