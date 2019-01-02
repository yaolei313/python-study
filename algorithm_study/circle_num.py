#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int

        0 - 1
        1 - 2
        2 - 4
        3 - 4
        """
        stu_count = len(M)
        if stu_count == 0:
            return 0

        count = 0

        for i in range(stu_count):
            if M[i][i] != 0:
                stack = [i]
                while len(stack) != 0:
                    item = stack.pop()
                    M[item][item] = 0
                    for j in range(stu_count):
                        if j == item:
                            continue
                        if M[item][j] == 1 and M[j][j] != 0:
                            stack.append(j)

                count += 1

        return count


if __name__ == "__main__":
    t = Solution()
    input_grid = [[1, 0, 0, 1],
                  [0, 1, 1, 0],
                  [0, 1, 1, 1],
                  [1, 0, 1, 1]]
    tcount = t.findCircleNum(input_grid)
    print("{}".format(tcount))

# 1,4
# 2,3
# 3,4
