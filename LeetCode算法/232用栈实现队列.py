# -*- coding: utf-8 -*-
# @Time     : 2019/3/6 11:11
# @Author   : Junee
# @FileName: 232用栈实现队列.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack, self.outstack = [ ], [ ]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        return self.outstack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return self.outstack[ -1 ]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.instack and not self.outstack

    def move(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())