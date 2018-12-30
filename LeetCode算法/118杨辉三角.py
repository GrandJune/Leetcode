# -*- coding: utf-8 -*-
# @Time     : 2018/12/30 17:24
# @Author   : Junee
# @FileName: 118杨辉三角.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if not numRows:
        return []
    if numRows == 1:
        return [[1]]
    res = [[1],[1,1]]
    for i in range(2,numRows):
        temp = [(res[i-1][j] + res[i-1][j+1]) for j in range(len(res[i-1])-1)]
        temp = [1] + temp + [1]
        res.append(temp)
    return res
a = generate(5)
print(a)