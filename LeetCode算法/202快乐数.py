# -*- coding: utf-8 -*-
# @Time     : 2019/1/6 15:26
# @Author   : Junee
# @FileName: 202快乐数.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = list(str(n))
        count = 0
        for each in n:
            count += int(each) * int(each)
        if count == 1:
            return True
        elif count in [4,16,37,58,89,145,42,20]:  # 所有的快乐数都会陷入这个循环
            return False
        else:
            return self.isHappy(count)