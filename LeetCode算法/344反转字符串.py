# -*- coding: utf-8 -*-
# @Time     : 2018/12/9 16:22
# @Author   : Junee
# @FileName: 344反转字符串.py
# @Software  : PyCharm
# Observing PEP 8 coding style
s = 'asd'
# 方法一：对字符串进行切片[::-1],-1表示逆序
print(s[::-1])
# 方法二；转化为列表进行操作
s = list(s)
# 逆序的两种写法，一使用切片；二使用reverse()内置函数
print(s[::-1])
s.reverse()
s = ''.join(s)
print(s)