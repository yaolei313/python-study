#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            x = -x
            negative = True

        min_value = 2 ** 31
        max_value = min_value - 1

        result = 0
        while x != 0:
            remainder = x % 10
            x = x // 10
            if negative and result > (min_value - remainder) // 10:
                return 0
            if not negative and result > (max_value - remainder) // 10:
                return 0
            result = result * 10 + remainder

        if negative:
            return -result
        return result
