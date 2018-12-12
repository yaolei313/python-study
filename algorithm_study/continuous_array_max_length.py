#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            max_length = 1

            current_len = 1
            # current_step = -1
            for i in range(len(nums) - 1):
                step = nums[i + 1] - nums[i]
                if step > 0:
                    current_len += 1
                    # 要的不是等差数列
                    # elif step == current_step:
                    #    current_len += 1
                    # else:
                    #    if current_len > max_length:
                    #        max_length = current_len
                    #    # 重新开始
                    #    current_step = -1
                    #    current_len = 1
                else:
                    if current_len > max_length:
                        max_length = current_len
                    # 重新开始
                    # current_step = -1
                    current_len = 1
            if current_len > max_length:
                max_length = current_len
            return max_length


if __name__ == "__main__":
    # input_array = [4, 5, 6, 7, 0, 1, 2]
    input_array = [1, 2, 5, 8, 0]
    t = Solution()
    output = t.findLengthOfLCIS(input_array)
    print("result count:{0}".format(output))
