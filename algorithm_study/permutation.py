#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 定义ai为第1列固定后需要多少种组合
        # 第k大意为这前面有k-1种组合
        # (a1-1)*(n-1)!+(a2-1)*(n-2)!+...+(a[n-1]-1)*1! = k - 1

        # 计算(n-1)!并缓存
        result = ""

        cache = {}
        value = 1
        for i in range(1, n):
            if i == 1:
                value = 1
            else:
                value *= i
            cache[i] = value

        choose_list = list(range(1, n + 1))

        total = k - 1
        idx = n - 1
        while idx > 0:
            group = total // cache[idx]
            result += self.chooseAndDel(choose_list, group + 1)
            total = total % cache[idx]
            n -= 1
            idx -= 1

        result += self.chooseAndDel(choose_list, 1)
        return result

    def chooseAndDel(self, choose_list, seq):
        numb = choose_list[seq - 1]
        del choose_list[seq - 1]
        return str(numb)


if __name__ == "__main__":
    t = Solution()
    tstr = t.getPermutation(4, 9)
    print("{}".format(tstr))
