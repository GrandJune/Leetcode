# -*- coding: utf-8 -*-
# @Time     : 2019/1/20 21:55
# @Author   : Junee
# @FileName: 690员工的重要性.py
# @Software  : PyCharm
# Observing PEP 8 coding style
# BFS 广度优先搜索
from collections import deque
class Solution:
    def getImportance(self, employees, i):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {i.id:i for i in employees}
        visited = set()
        ret = 0
        q = deque()
        q.append(dic[i])
        while q:
            cur = q.popleft()
            ret+=cur.importance
            visited.add(cur.id)
            for i in cur.subordinates:
                if i not in visited:
                    q.append(dic[i])
        return ret