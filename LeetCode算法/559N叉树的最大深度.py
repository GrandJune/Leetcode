# -*- coding: utf-8 -*-
# @Time     : 2018/12/27 23:43
# @Author   : Junee
# @FileName: 559N叉树的最大深度.py
# @Software  : PyCharm
# Observing PEP 8 coding style
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # 递归
        # if not root:
        #     return 0
        # if not root.children:
        #     return 1
        # return max([self.maxDepth(x) for x in root.children]) + 1

        # 迭代
        if not root:
            return 0
        cur = root.children
        count = 1
        while cur:
            children_list = [ ]
            count += 1
            for each in cur:
                if len(each.children) != 0:
                    children_list += each.children
            cur = children_list
        return count