# -*- coding: utf-8 -*-
# @Time     : 2019/1/3 17:14
# @Author   : Junee
# @FileName: 496下一个更大的元素.py
# @Software  : PyCharm
# Observing PEP 8 coding style


def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    temp = {}
    res = []
    if (not nums) or (not findNums):
        return []
    for i in range(len(nums)-1):
        temp[nums[i]] = nums[i+1::]
    temp[nums[-1]] = [-float('inf')]
    print(temp)
    j = 0
    while j < len(findNums):
        num = -1    # 这类问题，如果整个循环都没有满足的，返回-1；如果有满足条件的，改变返回值的写法：
        # 先在循环前定义一个-1，再在条件内修改该变量，最后取这个变量的值
        for n in temp[findNums[j]]:
            if n > findNums[j]:
                num = n
                break
        res.append(num)
        j += 1
        # print(j)
    return res

# a = [1,3,5,2,4]
# b = [5,4,3,2,1]
a = [4,1,2]
b = [1,2,3,4]

res = nextGreaterElement(a,b)
print(res)