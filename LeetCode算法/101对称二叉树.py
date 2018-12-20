# -*- coding: utf-8 -*-
# @Time     : 2018/12/20 15:44
# @Author   : Junee
# @FileName: 101对称二叉树.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 递归方法
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.is_duichen(root.left,root.right)
        else:
            return True
    def is_duichen(self,left,right):
        if left and right:
            if left.val == right.val:
                return self.is_duichen(left.left,right.right) and self.is_duichen(left.right,right.left)
            else:
                return False
        else:
            return not left and not right  #就算有空值，也可以说对称二叉树，所以要把空值变成非空，
            # 接着递归有值的那一侧子树

# 迭代法
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            value = [i.val if i else None for i in queue]
            if value != value[::-1]:
                return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
