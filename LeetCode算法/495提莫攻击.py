# -*- coding: utf-8 -*-
# @Time     : 2019/1/17 19:09
# @Author   : Junee
# @FileName: 495提莫攻击.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        wakeup, sleep, prevtime = 0, 0, 0
        for time in timeSeries:
            if time >= wakeup:
                sleep += duration
            else:
                sleep += (time - prevtime)
            wakeup = time + duration
            prevtime = time
        return sleep