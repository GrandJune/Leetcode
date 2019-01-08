# -*- coding: utf-8 -*-
# @Time     : 2019/1/8 21:01
# @Author   : Junee
# @FileName: 766拓普利兹矩阵.py
# @Software  : PyCharm
# Observing PEP 8 coding style
def isToeplitzMatrix(matrix):
    if len(matrix) == 0:
        print('T1')
        return True
    elif (len(matrix) == 1) | (len(matrix[0]) == 1):
        print('T2')
        return True
    print(matrix)
    for i in range(len(matrix)-1):
        if matrix[i][0] != matrix[i+1][1]:
            print('F1')
            return False
    for j in range(len(matrix[0])-1):
        if matrix[0][j] != matrix[1][j+1]:
            print('F2')
            return False
    m4 = [[ matrix[ i ][ j ] for j in range(1, len(matrix[ 0 ])) ] for i in range(1, len(matrix)) ]
    return isToeplitzMatrix(m4)
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
matrix_2 =[
    [53,64,90,98,34],
    [91,53,64,90,98],
    [17,91,53,64,0]
]
isToeplitzMatrix(matrix_2)

# m2 = matrix[1::]
# m3 = m2[::][1::]
# m4 = [[matrix[i][j] for j in range(1,len(matrix[0]))] for i in range(1,len(matrix))]   # 取子矩阵
# m5 = [[matrix[i][j] for i in range(1,len(matrix))] for j in range(1,len(matrix[0]))]   # 取子矩阵的转置
# print(m4)
# print(m5)

# 以上属于想复杂了，不过多找到一种递归使用子矩阵的思路
# 下面这种是简单的暴力搜索就行了，反而速度快
def isToeplitzMatrix(matrix):
    m = len(matrix)
    n = len(matrix[ 0 ])
    for i in range(m - 1):
        for j in range(n - 1):
            if matrix[ i ][ j ] != matrix[ i + 1 ][ j + 1 ]:
                return False
    return True
