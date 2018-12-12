#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dindex = {}
    for i in range(len(nums)):
        if target - nums[i] in dindex:
            return [i, dindex[target - nums[i]]]
        dindex[nums[i]] = i
    raise Exception('not two values')


if __name__ == "__main__":
    input_array = [3, 2, 4]
    target_number = 6
    output_array = twoSum(input_array, 6)
    print(output_array)
