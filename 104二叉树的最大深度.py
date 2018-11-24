# -*- coding: utf-8 -*-
# @Time     : 2018/11/24 21:59
# @Author   : Junee
# @FileName: 104二叉树的最大深度.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# 方法一：递归算法，每次返回该节点的深度：深度优先
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1

# 在栈的帮助下，将递归转化为迭代
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [ ]
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != [ ]:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth