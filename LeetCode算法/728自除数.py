# -*- coding: utf-8 -*-
# @Time     : 2018/12/17 0:00
# @Author   : Junee
# @FileName: 728自除数.py
# @Software  : PyCharm
# Observing PEP 8 coding style
a = []
a.append(21)
# for each in range(1,101):
#     a.append(each)
res = []
for ai in a:
    # b = list(map(int,str(ai)))
    b = map(int,str(ai))
    print(b)
    flag = 1
    for each in b:
        if each:
            if ai % each != 0:
                flag = 0
                break
        else:
            flag = 0
    if flag:
        res.append(ai)
print(res)
