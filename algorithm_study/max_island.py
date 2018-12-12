#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_size = 0
        row = len(grid)
        if row == 0:
            return 0
        column = len(grid[0])

        for i in range(row):
            for j in range(column):
                size = self.findAndDestoryIsland(grid, row, column, i, j)
                if size is not None and size > max_size:
                    max_size = size
        return max_size

    def findAndDestoryIsland(self, grid, row, column, i, j):
        if grid[i][j] == 0:
            return None
        size = 0
        stack = [(i, j)]
        grid[i][j] = 0

        while len(stack) > 0:
            k, v = stack.pop(0)
            size += 1
            if k - 1 >= 0 and grid[k - 1][v] == 1:
                grid[k - 1][v] = 0
                stack.append((k - 1, v))
            if k + 1 < row and grid[k + 1][v] == 1:
                grid[k + 1][v] = 0
                stack.append((k + 1, v))
            if v - 1 >= 0 and grid[k][v - 1] == 1:
                grid[k][v - 1] = 0
                stack.append((k, v - 1))
            if v + 1 < column and grid[k][v + 1] == 1:
                grid[k][v + 1] = 0
                stack.append((k, v + 1))

        return size


if __name__ == "__main__":
    # input_array = [-1, 0, 1, 2, -1, -4]
    input_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    input_grid2 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    t = Solution()
    output = t.maxAreaOfIsland(input_grid2)
    print("result:{0}".format(output))
