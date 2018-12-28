# -*- coding: utf-8 -*-
# @Time     : 2018/12/28 23:49
# @Author   : Junee
# @FileName: 700二叉搜索树中的搜索.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 递归法
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        que=[]
        que.append(root)
        if root is None:return []
        while len(que):
            node=que.pop(0)
            if node.val==val:
                return node
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        return None

# 迭代法
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        que=[]
        que.append(root)
        if not root:
            return None
        while len(que):
            node=que.pop(0)
            if node.val == val:
                return node
            elif (node.val > val) and (node.left):
                que.append(node.left)
            elif (node.val < val) and (node.right):
                que.append(node.right)
            else:
                return None