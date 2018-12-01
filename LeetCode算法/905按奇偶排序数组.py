# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 22:33
# @Author   : Junee
# @FileName: 905按奇偶排序数组.py
# @Software  : PyCharm
# Observing PEP 8 coding style
def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    even = [ ]
    odd = [ ]
    for each in A:
        if each % 2 == 0:
            even.append(each)
        else:
            odd.append(each)
    even.extend(odd)
    # return even.extend(odd)   # 常见的错误，返回None，应该是返回修改后的even列表
    # 类似的错误还有，返回a.append(b)，正确的做法应该是a.append(b)  return a
    return even

# 一个有趣的解法，使用冒泡排序的思路
def sortArrayByParity_bubble(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    i = 0
    for j in range(len(A)):
        if A[j] % 2 == 0:   # 这里本来还加了i!=j的条件，会出现错误，因为当第一个元素是偶数时会导致i没有自增
            A[i],A[j] = A[j],A[i]
            i += 1
        print(A)
    return A

# A = [1,2,3,4]
A = [0,1,2]
# res = sortArrayByParity(A)
res = sortArrayByParity_bubble(A)
print(res)