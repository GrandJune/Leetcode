# -*- coding: utf-8 -*-
# @Time     : 2018/11/23 9:39
# @Author   : Junee
# @FileName: 最长公共前缀.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         start = 0
#         strs_len = [len(str) for str in strs]
#         min_str_len = min(strs_len)
#         index_ = strs_len.index(min_str_len)
#         for i in range(len(strs)):
#             if strs[i][start] == strs[index_][start]:
#                 start += 1
#             if start >= min_str_len:
#                 break
#         if start == 0:
#             return ''
#         else:
#             return start


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    start = 0
    if '' in strs:
        return ''
    if len(strs) == 0:
        return ''
    strs = list(filter(None, strs))
    strs_len = [ len(str) for str in strs ]
    min_str_len = min(strs_len)
    index_ = strs_len.index(min_str_len)
    flag = 0
    while start < min_str_len:# 确定嵌套循环的结构，先循环的是字符串的每一位，再循环每个列表元素（先确定思路）
        for i in range(len(strs)):
            if strs[ i ][ start ] != strs[ index_ ][ start ]:
                return strs[ 0 ][ 0:start ] # 满足就跳过，不满足就结束类型的算法，只需要写!=条件语句加return
        start += 1
    return strs[0][0:start]

# strs = ["flower","flow","flight"]
# strs = [""]
# strs = ["c","c"]
strs = ["","b"]
re = longestCommonPrefix(strs)
print(re)
# print(len(strs))

# str = ['','']
# print(str[0])