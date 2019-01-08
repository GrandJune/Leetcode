# -*- coding: utf-8 -*-
# @Time     : 2019/1/8 21:33
# @Author   : Junee
# @FileName: 566重塑矩阵.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if len(nums) == 0:
        return []
    if r*c != len(nums)*len(nums[0]):
        return nums
    nums_2 = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
    print(nums_2)
    res = []
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(nums_2.pop(0))
        res.append(temp)
    return res
nums = [[1,2,3,4]]
# nums_2 = [ nums[ i ][ j ] for i in range(len(nums)) for j in range(len(nums[0])) ]
# print(nums_2)
r = 2
c = 2
res = matrixReshape(nums,r,c)
print(res)

from itertools import chain
# itertools模块提供了多种迭代器，chain用来把多个可迭代对象合并成一个大的整体；
# 其实就是并集操作，打开边界，最后合并只有一个[]
# 对于列表相当于用list_sum += list_1 + list_2 + ...
def matrixReshape(nums, r, c):
    result = [ ]
    # num = list(chain(*nums))
    # 相当于一句顶下面的三句话
    num = []
    for each in num:
        num += each
    num = [each for each in nums]

    size = len(num)
    if size != r * c:
        return nums
    else:
        for i in range(r):
            tem = [ ]
            for j in range(c):
                tem.append(num[ j + i * c ])
            result.append(tem)
        return result