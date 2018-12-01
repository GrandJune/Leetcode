# -*- coding: utf-8 -*-
# @Time     : 2018/8/10 23:48
# @Author   : Junee
# @FileName: 无重复字符的最大子串.py
# @Software  : PyCharm
# Observing PEP 8 coding style


# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     temp = [ ]
#     len_list = [ ]
#     n = 0
#     if len(s) == 1:
#         return 1
#     elif len(s) == 0:
#         return 0
#     else:
#         for i in range(0, len(s)):
#             if s[ i ] not in temp:
#                 n += 1
#                 temp.append(s[ i ])
#
#             else:
#                 len_list.append(n)
#                 n = 1
#                 # i -= 1  ##这个修改i的操作不影响循环使用的计数，也就是无法实现回到上一层循环
#                 temp.clear()
#                 temp.append(s[i])
#
#         len_list.append(n)  # 防止都没有重复导致不进入else语句块
#
#         # len_list.sort()
#         len_ = len_list[ -1 ]
#         print(len_list)
#         return len_
#
# run = lengthOfLongestSubstring(s="abbcdbf")
# print(run)


##试图解决回滚问题，必须回滚到上一个相同的元素处
##方法三：求每两个相同元素之间的距离就可以了
##方法三存在问题，abb就没法求了，因为a没包含在两个b之间
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     len_list = [ ]
#     if len(s) == 1:
#         return 1
#     elif len(s) == 0:
#         return 0
#     else:
#         temp_dict = {}
#         n = 0
#         last_loc = 0
#         for each in s:
#             if each not in temp_dict.keys():
#                 temp_dict[ each ] = n
#                 # if n == len(s) - 1:
#                 #     len_list.append(n + 1)  ##存在问题，都不存在重复值时不进入else，导致len_list为空
#                 #但是这么写有错误，如果最后一段没有重复，就会误认为整个字符串没有重复，如aab
#                 ##解决办法，引入last_loc，标记上一次重复字符的位置，在循环结束时执行一下
#             else:
#                 len_ = n - temp_dict[each]  ##还存在问题，如果有多次重复，会都减去第一个重复的位置，导致距离不实
#                 temp_dict[each] = n  ##解决办法：更新最新的这个重复的位置
#                 last_loc = n
#                 len_list.append(len_)
#             n += 1
#         len_ = n - last_loc
#         len_list.append(len_)  #循环结束后再加入一个，避免最后没有进入else语句块而漏掉最后一个长度
#         print(len_list)
#         print("*****")
#
#         m = 0
#         temp_list = []  #从头算一遍不重复的长度，不回滚，与上面那个结合求出所有的长度
#         for i in range(0, len(s)):
#             if s[i] not in temp_list:
#                 m += 1
#                 temp_list.append(s[i])
#
#             else:
#                 len_list.append(m)
#                 m = 1
#                 # i -= 1  ##这个修改i的操作不影响循环使用的计数，也就是无法实现回到上一层循环
#                 temp_list.clear()
#                 temp_list.append(s[i])
#
#         print(len_list)
#         len_list.sort()
#         result_len = len_list.pop()
#     return result_len
#
#
# run = lengthOfLongestSubstring(s="abba")
# print(run)

#仍然报错，因为我们求了两个相同字符之间的长度，没有考虑到两个相同字符中间可能还有相同字符导致出错

len_list = []
def func(s,start=0):
    temp = []
    m = start
    for n in range(start,len(s)):
        if s[n] not in temp:
            temp.append(s[n])
            if n == len(s) - 1:
                len_list.append(len(temp))
                return m - start + 1
        elif n in temp:
            len_list.append(len(temp))
            return m
        m += 1


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    ##使用滑动窗口的思想

    if len(s) == 0:
        return 0
    else:
        index = 0
        len_ = len(s)
        # print(len_)
        # print(index<len_)
        while True:
            index = func(s,start=index)
            print(index)



lengthOfLongestSubstring(s="abcabcbb")
print(len_list)
