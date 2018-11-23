# -*- coding: utf-8 -*-
# @Time     : 2018/11/23 0:20
# @Author   : Junee
# @FileName: 无重复字符的最长子串.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# 使用哈希表，即Python中的字典
# class Solution:
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     n = len(s)
#     if n == 0:
#         return 0
#     else:
#         location = 0
#         start = 0
#         length = 1
#         dic = {}
#         for i in range(n):
#             current = s[i]
#             if current not in dic.keys():
#                 dic[current] = i
#             else:
#                 # if dic[current] + 1 > start:   # 此处加1 是因为一开始start 和current都在0处，不加一的话，这时候start就不转换了
#                 start = dic[current] + 1    #其实不加的话也还是可以的，默认current >= start
#                 dic[current] = i
#             if i - start + 1 > length:
#                 length = i - start + 1
#             print(length,i,start)
#
#         return length

# 针对"aabaab!bb"报错
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     n = len(s)
#     if n == 0:
#         return 0
#     else:
#         # location = 0
#         start = 0
#         length = 1
#         dic = {}
#         for i in range(n):
#             current = s[i]
#             if current not in dic.keys():
#                 dic[current] = i
#             else:
#                 print("重复")
#                 if dic[current] + 1 > start:
#                     start = dic[current] + 1
#                     print('start变化，start= %d' % start)
#                     # dic[current] = i  # 上一版中的错误，这个更新操作不能在条件语句内部，这里还是有重复代码，这个操作是每次循环都要的
#                 dic[ current ] = i
#             if i - start + 1 > length:
#                 length = i - start + 1
#             print(length,i,start)
#             for key,value in dic.items():
#                 print('**第%d次循环*' % i,key,value)
#
#         return length
#
# s = "abcabcdbb"
# s = 'abba'
# s = "aabaab!bb"
# s = 'ab!bb'
# result = lengthOfLongestSubstring(s)
# print(result)

# 修正精简版本
# 修正不加current在前的条件判断，当abba时会出错，因为a的第一个位置在0出，导致start又从2处移回到0处，
# class Solution:
#     def lengthOfLongestSubstring(self,s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         start = 0
#         length = 0  # 默认长度为零就可以不用判断是否为空
#         dic = {}
#         for i in range(n):
#             current = s[i]
#             if current not in dic.keys():
#                 dic[current] = i
#             else:
#                 if dic[current] + 1 > start:   # 此处加+1条件判断，保证current+1一定在start的右边，start只能向右移动
#                 start = dic[current] + 1
#                 dic[current] = i
#             if i - start + 1 > length:
#                 length = i - start + 1
#             print(length,i,start)
#
#         return length


# 简洁版本
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_len = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[ s[ i ] ] + 1
            else:
                max_len = max(max_len, i - start + 1)
            used[s[i]] = i

        return max_len