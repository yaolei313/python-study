#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        dict_order = {"I": 1, "V": 2, "X": 3, "L": 4, "C": 5, "D": 6, "M": 7}
        dict_spec = {"X": 3,"C": 5, "M": 7}

        if len(s) == 1:
            return dict_value[s]

        result = 0

        i = 0
        j = 1
        while j < len(s):

            if dict_order[s[i]] > dict_order[s[j]]:
                result += dict_value[s[i]]
                i = i + 1
                j = i + 1
            elif dict_order[s[i]] == dict_order[s[j]]:
                result += 2 * dict_value[s[i]]
                i = j + 1
                j = i + 1
            else:
                result += dict_value[s[j]] - dict_value[s[i]]
                i = j + 1
                j = i + 1

        if i < len(s):
            result += dict_value[s[i]]
        return result
