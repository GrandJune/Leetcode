# -*- coding: utf-8 -*-
# @Time     : 2019/1/1 21:58
# @Author   : Junee
# @FileName: 206翻转链表.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 迭代法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        pre = None
        while p:
            q = p.next
            p.next = pre
            pre = p
            p = q
        return pre