# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 23:08
# @Author   : Junee
# @FileName: 349两个数组的交集.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    len_1 = len(nums1)
    len_2 = len(nums2)
    if len_1 * len_2 == 0:
        return [ ]
    result = set()
    for each in nums1:
        if each in nums2:
            result.add(each)

    return list(result)

# 简单写法：集合自带的&操作（但是本地测试结果表明还是上一种写法用时短）
def intersection_set(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(nums1) & set(nums2))

import time
num1 = [9,4,9,4]
num2 = [1,2,3,4]
t0 = time.clock()
result_1 = intersection(num1,num2)
t1 = time.clock()
print(result_1,t1-t0)
t2 = time.clock()
result_2 = intersection_set(num1,num2)
t3 = time.clock()
print(result_2,t3-t2)

# 本地测试结果表明第一种方式快，但是LeetCode运行确实第二种速度快；
# 说明LeetCode运行时间可能还跟代码量有关
