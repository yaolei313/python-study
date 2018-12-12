#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k]
        end_index = k // 2 - 1
        for i in range(end_index, -1, -1):
            self.min_heapify(min_heap, k, i)

        for item in nums[k:]:
            if item > min_heap[0]:
                min_heap[0] = item
                self.min_heapify(min_heap, k, 0)
        return min_heap[0]

    def min_heapify(self, heap, size, i):
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            minimum = i
            if left <= size - 1 and heap[left] < heap[i]:
                minimum = left
            if right <= size - 1 and heap[right] < heap[minimum]:
                minimum = right
            if minimum != i:
                heap[i], heap[minimum] = heap[minimum], heap[i]
                i = minimum
            else:
                break


if __name__ == "__main__":
    input_array = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    t = Solution()
    output = t.findKthLargest(input_array, 4)
    print("result count:{0}".format(output))
