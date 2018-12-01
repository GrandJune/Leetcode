# -*- coding: utf-8 -*-
# @Time     : 2018/8/10 18:37
# @Author   : Junee
# @FileName: 两数相加.py
# @Software  : PyCharm
# Observing PEP 8 coding style

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len_1 = len(l1)
        len_2 = len(l2)
        len_max = max(len_1,len_2)
        len_min = min(len_1,len_2)
        flag = 0
        result_list = []
        for i in range(0,len_min):
            sum_ = l1[i] + l2[i] + flag
            flag = 0
            if sum_ >= 10:
                s = sum_ % 10
                flag = sum_ // 10
            else:
                s = sum_
            result_list.append(s)

        if len_1 < len_2:
            for i in range(len_min,len_max):
                sum_ = l2[i] + flag
                flag = 0
                if sum_ >= 10:
                    s = sum_ % 10
                    flag = sum_ // 10
                else:
                    s = sum_
                result_list.append(s)

        if len_1 > len_2:
            for i in range(len_min,len_max):
                sum_ = l1[i] + flag
                flag = 0
                if sum_ >= 10:
                    s = sum_ % 10
                    flag = sum_ // 10
                else:
                    s = sum_
                result_list.append(s)

        return result_list