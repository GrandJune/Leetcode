# -*- coding: utf-8 -*-
# @Time     : 2019/1/30 23:26
# @Author   : Junee
# @FileName: 543二叉树的直径.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
         """
        self.ans = 0

        def helper(root):
            if not root:
                return 0
            L = helper(root.left)
            R = helper(root.right)
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1

        helper(root)
        return self.ans