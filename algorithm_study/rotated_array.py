#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.specialBinarySearch(nums, 0, len(nums) - 1, target)

    def specialBinarySearch(self, num, l, r, target):
        if l > r:
            return -1
        if l == r:
            if num[l] == target:
                return l
            else:
                return -1
        mid = (l + r) // 2
        if num[mid] == target:
            return mid
        # 2个元素时
        if mid == l:
            if num[r] == target:
                return r
            else:
                return -1

        # 必须3个元素
        if num[mid] > num[l] > num[r]:
            if num[l] == target:
                return l
            if num[r] == target:
                return r
            if num[l] < target < num[mid]:
                return self.specialBinarySearch(num, l + 1, mid - 1, target)
            else:
                return self.specialBinarySearch(num, mid + 1, r - 1, target)
        elif num[mid] < num[r] < num[l]:
            if num[l] == target:
                return l
            if num[r] == target:
                return r
            if num[mid] < target < num[r]:
                return self.specialBinarySearch(num, mid + 1, r - 1, target)
            else:
                return self.specialBinarySearch(num, l + 1, mid - 1, target)
        else:
            # 正常序列
            if num[l] == target:
                return l
            if num[r] == target:
                return r
            if num[mid] > target:
                return self.specialBinarySearch(num, l + 1, mid - 1, target)
            else:
                return self.specialBinarySearch(num, mid + 1, r - 1, target)


if __name__ == "__main__":
    # input_array = [4, 5, 6, 7, 0, 1, 2]
    input_array = [3, 5, 1]
    t = Solution()
    output = t.search(input_array, 3)
    print("result count:{0}".format(output))
