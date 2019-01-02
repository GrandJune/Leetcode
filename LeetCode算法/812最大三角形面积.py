# -*- coding: utf-8 -*-
# @Time     : 2019/1/2 21:57
# @Author   : Junee
# @FileName: 812最大三角形面积.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def calc(a, b, c):
            x1, y1 = a[ 0 ], a[ 1 ]
            x2, y2 = b[ 0 ], b[ 1 ]
            x3, y3 = c[ 0 ], c[ 1 ]
            return abs(x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3) / 2.0
            # (x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)/2

        max_area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    a = points[ i ]
                    b = points[ j ]
                    c = points[ k ]
                    max_area = max(max_area, calc(a, b, c))
        return max_area