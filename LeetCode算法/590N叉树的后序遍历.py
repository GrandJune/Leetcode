# -*- coding: utf-8 -*-
# @Time     : 2018/12/22 22:58
# @Author   : Junee
# @FileName: 590N叉树的后序遍历.py
# @Software  : PyCharm
# Observing PEP 8 coding style
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# 递归法
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = []
        for child in root.children:
            result += self.postorder(child)
        result += [root.val]
        return result

# 迭代法
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res[::-1]