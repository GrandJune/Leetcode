# -*- coding: utf-8 -*-
# @Time     : 2019/3/1 20:04
# @Author   : Junee
# @FileName: 705设计哈希集合表.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# 主题思想，预留出一段足够宽的带宽(列表),就可以变成哈希表了，用空间换时间
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = [-1] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.t[key] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.t[key] = -1

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return (self.t[key] == 1)