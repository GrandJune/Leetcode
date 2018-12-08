# -*- coding: utf-8 -*-
# @Time     : 2018/12/8 23:50
# @Author   : Junee
# @FileName: 942增减字符串匹配.py
# @Software  : PyCharm
# Observing PEP 8 coding style
def diStringMatch( S):
    """
    :type S: str
    :rtype: List[int]
    """
    len_s = len(S)
    n_list = [ i for i in range(len_s + 1) ]
    S = list(S)
    i = 0
    result = [ ]
    while i < len_s:
        if S[ i ] == 'I':
            result.append(n_list.pop(0))
        else:
            result.append(n_list.pop())
        i += 1
    result.append(n_list[ 0 ])
    return result