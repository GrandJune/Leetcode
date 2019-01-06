# -*- coding: utf-8 -*-
# @Time     : 2019/1/6 14:39
# @Author   : Junee
# @FileName: 13罗马数字转整数.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict_nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    s = list(s)
    count = 0
    for i in range(len(s)-1):
        if dict_nums[s[i]] < dict_nums[s[i+1]]:
            count -= dict_nums[s[i]]
        else:
            count += dict_nums[s[i]]
    count += dict_nums[s[-1]]
    return count
s = 'IV'
num = romanToInt(s)
print(num)