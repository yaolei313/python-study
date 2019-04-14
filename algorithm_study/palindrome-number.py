#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        lst = []

        while x != 0:
            numb = x % 10

            if len(lst) == 0 and numb == 0:
                return False

            lst.append(numb)
            x = x // 10

        i = 0
        j = len(lst) - 1
        while i <= j:
            if lst[i] == lst[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

    def isPalindrome2(self, x: int):
        lst = []

        while x != 0:
            numb = x % 10
            lst.append(numb)
            x = x // 10

        print(lst)


if __name__ == "__main__":
    sol = Solution()
    rst = sol.isPalindrome(123456)
    print("result is {}".format(rst))
    rst = sol.isPalindrome(12345654321)
    print("result is {}".format(rst))
    rst = sol.isPalindrome(-121)
    print("result is {}".format(rst))
