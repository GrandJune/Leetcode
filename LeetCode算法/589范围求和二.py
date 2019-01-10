# -*- coding: utf-8 -*-
# @Time     : 2019/1/10 22:38
# @Author   : Junee
# @FileName: 589范围求和二.py
# @Software  : PyCharm
# Observing PEP 8 coding style

nums = [[0]*3]*3
# print(nums)
for i in range(2):
    for j in range(2):
        print(i,j,nums)
        nums[i][j] = 1
        # print(nums[i][j])
        print(i,j,nums)
        print('******')
# print(nums)

def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    nums = [[0]*m]*n
    for each in ops:
        nums = add_ops(nums,each[0],each[1])
    count = 0
    max_num = 0
    print(nums)
    for each in nums:
        for num in each:
            if num > max_num:
                max_num = num
                count = 1
            elif num == max_num:
                count += 1
                print(num,'**',count)
            else:
                pass
    return count
def add_ops(nums,a,b):
    print(nums)
    for r in range(a):
        for c in range(b):
            print(r,c,nums[r][c])
            nums[r][c] = 1
            print(r,c,nums[r][c])
            print('-------------')
    return nums

m, n = 3,3
operations = [[2,2]]
# res = maxCount(m,n,operations)
# print(res)

# 脑筋急转弯，只要找到最小的m 乘以最小的n就可以了
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m*n
        t1,t2 = zip(*ops)
        t1,t2 = min(t1),min(t2)
        return min(t1,m) * min(t2,n)