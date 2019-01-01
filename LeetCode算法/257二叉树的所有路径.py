# -*- coding: utf-8 -*-
# @Time     : 2019/1/1 21:38
# @Author   : Junee
# @FileName: 257二叉树的所有路径.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 比较烧脑的递归
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if (not root.left) and (not root.right):
            return [str(root.val)]
        paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        for i in range(len(paths)):
            paths[i] = str(root.val) + '->' + paths[i]
        return paths


class Solution:
    #@param {TreeNode} root
    #@return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val)+'->'+path
               for kid in (root.left,root.right) if kid
               for path in self.binaryTreePaths(kid)] or [str(root.val)]

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.ans = []
        if root is None:
            return self.ans
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans += path,
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))
        dfs(root, str(root.val))
        return self.ans