#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        longest = 1
        count_dict = dict()
        for i in nums:
            count_dict[i] = 1

        for j in nums:
            if count_dict[j] != 0:
                tlen = count_dict[j]
                current = j - 1
                while current in count_dict and count_dict[current] != 0:
                    tlen += 1
                    count_dict[current] = 0
                    current -= 1
                current = j + 1
                while current in count_dict and count_dict[current] != 0:
                    tlen += 1
                    count_dict[current] = 0
                    current += 1
                if tlen > longest:
                    longest = tlen
        return longest


if __name__ == "__main__":
    input_array = [100, 4, 200, 1, 3, 2]
    t = Solution()
    output = t.longestConsecutive(input_array)
    print("result:{0}".format(output))
