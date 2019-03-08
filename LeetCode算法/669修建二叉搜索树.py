# -*- coding: utf-8 -*-
# @Time     : 2019/3/8 22:58
# @Author   : Junee
# @FileName: 669修建二叉搜索树.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 二叉搜索树的定义，左侧结点小于根节点的值，右侧结点大于根节点的值
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif root.val > R:
            return self.trimBST(root.left,L,R)
        elif root.val < L:
            return self.trimBST(root.right,L,R)
        else:
            root.left = self.trimBST(root.left,L,R)
            root.right = self.trimBST(root.right,L,R)
            return root