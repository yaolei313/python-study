class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if n == 0:
            return self.findMedianSortedArrays(nums2, nums1)
        if m == 0:
            if n % 2 == 0:
                return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
            else:
                return nums2[n // 2]

        num3 = []
        i = 0
        j = 0
        while True:
            while i < m and nums1[i] <= nums2[j]:
                num3.append(nums1[i])
                i += 1
            if i == m:
                break
            while j < n and nums1[i] > nums2[j]:
                num3.append(nums2[j])
                j += 1
            if j == n:
                break
        while i < m:
            num3.append(nums1[i])
            i += 1
        while j < n:
            num3.append(nums2[j])
            j += 1

        if (m + n) % 2 == 0:
            return (num3[(m + n) // 2 - 1] + num3[(m + n) // 2]) / 2
        else:
            return num3[(m + n) // 2]


if __name__ == "__main__":
    sol = Solution()
    input_array1 = [1, 2]
    input_array2 = [3, 4]
    output = sol.findMedianSortedArrays(input_array1, input_array2)
    print(output)
