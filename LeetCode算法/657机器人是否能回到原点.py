# -*- coding: utf-8 -*-
# @Time     : 2018/11/27 22:57
# @Author   : Junee
# @FileName: 657机器人是否能回到原点.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    low, column = 0, 0
    for each in moves:
        if each == 'R':
            low += 1
        elif each == 'L':
            low -= 1
        elif each == 'U':
            column += 1
        else:
            column -= 1
    if low == 0 and column == 0:
        return True
    else:
        return False

# 简单写法
def judgeCircle_2(moves):
    """
    :type moves: str
    :rtype: bool
    """
    return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')

moves = 'RURULDLD'
print(judgeCircle_2(moves))