# -*- coding: utf-8 -*-
# @Time     : 2019/3/15 15:24
# @Author   : Junee
# @FileName: 1006笨阶乘.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """

        N1 = 1
        N2 = 2 * 1
        N3 = 3 * 2 / 1
        N4 = 4 * 3 / 2 + 1

        if N == 1:
            return N1
        elif N == 2:
            return int(N2)
        elif N == 3:
            return int(N3)
        elif N == 4:
            return int(N4)

        ret = N * (N - 1) // (N - 2) + (N - 3)

        final = N % 4

        if final == 1:
            ret -= N1
        elif final == 2:
            ret -= N2
        elif final == 3:
            ret -= N3

        for i in range(N - 4, final, -4):
            ret = ret - i * (i - 1) // (i - 2) + (i - 3)
        ret = int(ret)
        return ret