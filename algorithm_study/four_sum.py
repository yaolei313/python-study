#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = list()
        d_map = {}
        for i in range(len(nums)):
            d_map[nums[i]] = i

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for m in range(j + 1, len(nums) - 1):
                    balance = target - (nums[i] + nums[j] + nums[m])
                    if balance in d_map and d_map[balance] > m:
                        node = [nums[i], nums[j], nums[m], balance]
                        if node not in result:
                            result.append(node)

        return result


if __name__ == "__main__":
    t = Solution()
    input_array = [1, -2, -5, -4, -3, 3, 3, 5]
    target_number = -11
    output_array = t.fourSum(input_array, target_number)
    print(output_array)
