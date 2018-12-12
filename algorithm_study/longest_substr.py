#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        l = 0
        r = 1
        c_len = 1
        max = c_len
        while r < len(s):
            t = s.find(s[r], l, r)
            r += 1
            if t == -1:
                c_len += 1
            else:
                l = t + 1
                c_len = r - l
            if c_len > max:
                max = c_len
        return max


if __name__ == "__main__":
    sol = Solution()
    input_str = "abcad"
    output_len = sol.lengthOfLongestSubstring(input_str)
    print(output_len)
