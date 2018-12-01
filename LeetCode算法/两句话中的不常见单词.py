# -*- coding: utf-8 -*-
# @Time     : 2018/8/13 21:43
# @Author   : Junee
# @FileName: 两句话中的不常见单词.py
# @Software  : PyCharm
# Observing PEP 8 coding style
def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    result_list = [ ]
    words_A = A.split()
    words_B = B.split()
    A_dict = {}
    B_dict = {}
    for each in words_A:
        if each not in A_dict.keys():
            A_dict[ each ] = 1
        else:
            A_dict[ each ] += 1

    for each in words_B:
        if each not in B_dict.keys():
            B_dict[ each ] = 1
        else:
            B_dict[ each ] += 1

    print(A_dict)
    print(B_dict)

    for key, value in A_dict.items():
        if value == 1:
            if key in B_dict.keys():
                pass
            else:
                result_list.append(key)
                print(result_list)

    for key, value in B_dict.items():
        if value == 1:
            if key in A_dict.keys():
                pass
            else:
                result_list.append(key)
                print(result_list)

    return result_list


A = "this apple is sweet"
B = "this apple is sour"
run = uncommonFromSentences(A,B)
print(run)