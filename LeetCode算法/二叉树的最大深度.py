# -*- coding: utf-8 -*-
# @Time     : 2018/12/14 23:29
# @Author   : Junee
# @FileName: 二叉树的最大深度.py
# @Software  : PyCharm
# Observing PEP 8 coding style


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0