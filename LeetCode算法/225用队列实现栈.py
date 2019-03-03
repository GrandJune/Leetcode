# -*- coding: utf-8 -*-
# @Time     : 2019/3/4 0:03
# @Author   : Junee
# @FileName: 225用队列实现栈.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = [ ]

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.s.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.s.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.s[ -1 ]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.s == [ ]