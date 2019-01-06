# -*- coding: utf-8 -*-
# @Time     : 2019/1/6 15:46
# @Author   : Junee
# @FileName: 100相同的树.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False
        else:
            return False