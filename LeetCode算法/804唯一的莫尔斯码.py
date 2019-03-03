# -*- coding: utf-8 -*-
# @Time     : 2019/3/4 0:14
# @Author   : Junee
# @FileName: 804唯一的莫尔斯码.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mors = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        aws = 0
        for each in words:
            temp = [ord(i)-97 for i in each]
            strings = [mors[i] for i in temp]
            string = ''.join(strings)
            if string not in res:
                res.append(string)
                aws += 1
        return aws