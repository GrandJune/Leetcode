# -*- coding: utf-8 -*-
# @Time     : 2019/1/9 19:12
# @Author   : Junee
# @FileName: 965单值二叉树.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if (root.left) and (root.right):
            if root.left.val == root.right.val:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            else:
                return False
        elif (not root.left) and (root.right):
            if root.val == root.right.val:
                return self.isUnivalTree(root.right)
            else:
                return False
        elif (root.left) and (not root.right):
            if root.val == root.left.val:
                return self.isUnivalTree(root.left)
            else:
                return False
        return True

# 简介的递归写法
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = [ ]

        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(res)) == 1