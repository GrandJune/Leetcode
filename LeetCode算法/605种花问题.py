# -*- coding: utf-8 -*-
# @Time     : 2019/2/19 23:04
# @Author   : Junee
# @FileName: 605种花问题.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    import math
    if n == 0:
        return True
    count = 0
    mark_1,count_0 = 0,0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            mark_1 += 1
            count += math.ceil((count_0-mark_1)/2)
            count_0 = 0
            mark_1 = 1
        else:
            count_0 += 1
        if (i == len(flowerbed)-1) and (flowerbed[i] == 0):
            count += math.ceil((count_0-mark_1)/2)
        print(count,i)
    # print(count)
    return count >= n

a = [1,0,0,0,1]
n = 1
# res = canPlaceFlowers(a,n)



def canPlaceFlowers_2(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    def ceil(x):
        """
        由于服务器上面的python的ceil不对劲，所以重写了一个
        :param x:
        :return:
        """
        if x % 2 == 0:
            return x/2
        else:
            return (x+1)/2
    if n == 0:
        return True
    count = 0
    mark_1,count_0 = 0,0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            mark_1 += 1
            count += ceil(count_0-mark_1)
            if count < 0:
                count = 0
             # 这里的python环境有问题:ceil()函数，-1/2的结果是-1,1/2的结果是0
            count_0 = 0
            mark_1 = 1
        else:
            count_0 += 1
        if (i == len(flowerbed)-1) and (flowerbed[i] == 0):
            # print('ss') #之前没进来，少写了减一，最后一个是len()-1
            count += ceil(count_0-mark_1)
        print(count,i)
    return count >= n

b = [1,0,0,0,1,0,0,0]
m = 2
res_2 = canPlaceFlowers_2(b,m)
print(res_2)
# res = canPlaceFlowers(b,m)
# print(res)