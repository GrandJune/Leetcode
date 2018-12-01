# -*- coding: utf-8 -*-
# @Time     : 2018/11/25 23:49
# @Author   : Junee
# @FileName: 929独特的电子邮件地址.py
# @Software  : PyCharm
# Observing PEP 8 coding style

def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    real_add_set = set()
    for each in emails:
        print(each)
        local_one = each.split('@')[ 0 ]
        yuming_one = each.split("@")[ 1 ]
        print(yuming_one)
        real_local = ''
        for each in local_one:
            if each == '.':
                pass
            elif each == '+':
                break
            else:
                real_local += each
                # print(real_local)
        real_add = real_local + '@' + yuming_one
        # print(real_add)
        real_add_set.add(real_add)
    return len(real_add_set)

re = numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(re)
