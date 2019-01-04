# -*- coding: utf-8 -*-
# @Time     : 2019/1/4 18:59
# @Author   : Junee
# @FileName: 788旋转数字.py
# @Software  : PyCharm
# Observing PEP 8 coding style
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for each in range(1,N+1):
            each_str = list(str(each))
            flag = 1
            for i in range(len(each_str)):
                if each_str[i] == '2':
                    each_str[i] = '5'
                elif each_str[i] == '5':
                    each_str[i] = '2'
                elif each_str[i] == '6':
                    each_str[i] = '9'
                elif each_str[i] == '9':
                    each_str[i] = '6'
                elif each_str[i] in ['1','0','8']:
                    pass
                else:
                    flag = 0
                    break
            if flag and (''.join(each_str) != str(each)):
                # print(each)
                count += 1
        return count