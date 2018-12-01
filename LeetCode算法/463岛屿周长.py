# -*- coding: utf-8 -*-
# @Time     : 2018/11/22 21:58
# @Author   : Junee
# @FileName: 463岛屿周长.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# mycode_1
# 遍历列表，一个1四条边，如果上下左右有1，每个1减掉1个边长
# 缺陷：这样会重复遍历四周的1，每次只减掉1
# 最优算法先记住所有的1的位置，四周有1是减掉2个边长
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        recount = 0
        land_sum = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land_sum = land_sum+1
                    if i-1 >= 0:
                        if grid[i-1][j] == 1:
                            recount += 1
                    if j - 1 >= 0:
                        if grid[i][j-1] == 1:
                            recount += 1
                    if i + 1 < n:
                        if grid[i + 1][j] == 1:
                            recount += 1
                    if j+1 < m:
                        if grid[i][1+j] == 1:
                            recount += 1
        print(land_sum, recount)
        return land_sum*4-recount

# mycode_2
# 吸收最优算法的思想，规定查找方向避免重复查找
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        recount = 0
        land_sum = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land_sum = land_sum+1
                    if i + 1 < n:
                        if grid[i + 1][j] == 1:
                            recount += 1
                    if j + 1 < m:
                        if grid[i][j + 1] == 1:
                            recount += 1
        print(land_sum, recount)
        return land_sum * 4 - recount * 2
# 结果发现，规定查找方向以后反而用时更长 524ms，应该是循环的时间太长导致的

# mycode_2改:发现其实速度应该是受到服务器的状态影响的，没办法达到最快的270 ms
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        recount = 0
        land_sum = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land_sum = land_sum+1
                    if i + 1 < n and grid[i + 1][j]:
                            recount += 1
                    if j + 1 < m and grid[i][j + 1]:
                            recount += 1
        print(land_sum, recount)
        return land_sum * 4 - recount * 2

# 最快算法278ms
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        perimeter = 0
        island = ((i, j) for j in range(n) for i in range(m) if grid[i][j] == 1)  # 记录陆地的坐标
        for i, j in island:
            perimeter += 4
            if i + 1 < m and grid[i + 1][j]:    # 只看一遍，即向下向右查找，避免重复查找
                perimeter -= 2
            if j + 1 < n and grid[i][j + 1]:
                perimeter -= 2
        # perimeter += len(island) * 4
        # for i, j in island:
        #     if (i + 1, j) in island:
        #         perimeter -= 2
        #     if (i, j + 1) in island:
        #         perimeter -= 2
        return perimeter