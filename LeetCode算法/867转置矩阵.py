# -*- coding: utf-8 -*-
# @Time     : 2018/12/6 16:07
# @Author   : Junee
# @FileName: 867转置矩阵.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 涉及的细节，列表的复制
# A = [[1,2,3],[4,5,6]]
# B = A
# B.append([7,8,9])
# print(B)
# print(A)
# 输出的结果表明AB两个矩阵都被修改了，因此只用等号赋值的话，
# 其实指向的是同一段数据/内存
# C = A.copy()
# C.append([7,8,9])
# print(A)
# print(C)
# 使用copy()函数之后，对C进行修改不会改变原来的A
# 但是copy()函数是浅复制，对A进行修改的话可能会改变复制出来的C
# 如下：
# A.append([7,8,9])
# print(A)
# print(C)
# 使用列表内置的copy方法，是将新列表中的元素指向了与原列表相同的内存空间。
# 但是，如果列表中嵌套了列表，拷贝后的列表中嵌套的列表元素指针，
# 指向原列表中嵌套列表的整体地址，而不是指向嵌套列表中元素的内存地址。
# 当你修改嵌套列表的元素时，整个嵌套列表的地址没有改变，但是修改了元素的地址指针，
# 但是B没有整体复制到嵌套元素的地址指针，导致B的指针只能找到整个子列表，也就被莫名修改了。
# A = [[1, 'hello'], 3, 4]
# B = A.copy()
# A[0][0] = 2
# A[0] = [2,'hello']
# print(A)
# print(B)
# 可以看到，当修改了A中的[0][0]位置的元素时，B也会被影响
# 但是如果你修改整个A[0]，B就不会受到影响

# 深层拷贝
# import copy
# A =  [[1, 'hello'], 3, 4]
# B = copy.deepcopy(A)
# A[0][0] = 2
# print(A)
# print(B)
# 使用深层拷贝方式，修改A的元素就不会对B产生影响


def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """

    line = [0] * len(A)
    print(line)
    B = [line] * len(A[0])
    print(B)
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(i,j)
            B[ j][ i ] = A[ i ][ j ]
    return B
A = [[1,2,3],[4,5,6]]
C = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print(C)
B = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
D = [[[C[i][j][k] for i in range(len(C))] for j in range(len(C[0]))] for k in range(len(C[0][0]))] # n阶矩阵的转置，按照嵌套顺序写就可以了
# 因为先写的在嵌套里层
# B = [[A[j][i] for j in range(len(A[0]))] for i in range(len(A))]
print(D)
# print(len(A))
# print(len(A[0]))
# B = transpose(A)
# print(B)
# print([0]*len(A[0]))


