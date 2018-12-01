# -*- coding: utf-8 -*-
# @Time     : 2018/8/13 22:17
# @Author   : Junee
# @FileName: 平衡二叉树.py
# @Software  : PyCharm
# Observing PEP 8 coding style

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        def depth_search(root):
            if root == None:
                return 0
            leftValue = depth_search(root.left)
            if leftValue == -1:
                return -1
            rightValue = depth_search(root.right)
            if rightValue == -1:
                return -1
            if abs(leftValue-rightValue) > 1:
                return -1
            return 1+max(leftValue, rightValue)
        value = depth_search(root)
        if value == -1:
            return False
        else:
            return True