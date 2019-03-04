# -*- coding: utf-8 -*-
# @Time     : 2019/3/4 18:34
# @Author   : Junee
# @FileName: 237删除链表中的结点.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 提供了一种很好的思想，将结点的值修改成下个结点的值，并指向下下个结点，就可以达到删除该节点的效果
# 存在一个问题：如果访问原来的下一个结点，还是能正常访问下去整个链表。
# 变成了存在两个相同的链表结点，或者说链表多了一个分支，分支上的两个结点相同
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next  = node.next.next