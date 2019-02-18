# -*- coding: utf-8 -*-
# @Time     : 2019/2/18 16:15
# @Author   : Junee
# @FileName: 292Nim游戏.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True
# 尽量拿掉之后剩下4的倍数，对手拿1你就拿3，总是凑成4那么一定是先手赢
# 所以如果一开始就是4的倍数就是先手输
#一行代码
# return n % 4 != 0