# -*- coding: utf-8 -*-
# @Time     : 2018/12/31 23:22
# @Author   : Junee
# @FileName: 107二叉树的层次遍历.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 击败了百分之百的用户！！！
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        res_nodes = [[root]]
        i = 0
        while True:
            temp = []
            nodes = []
            for current in res_nodes[i]:
                if current.left:
                    temp.append(current.left.val)
                    nodes.append(current.left)
                if current.right:
                    temp.append(current.right.val)
                    nodes.append(current.right)
            if len(temp):
                res.append(temp)
                res_nodes.append(nodes)
            else:
                break
            i += 1

        res.reverse()
        return res