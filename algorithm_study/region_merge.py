# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[{},{}]".format(self.start, self.end)


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None:
            return []
        elif len(intervals) == 1:
            return intervals

        # self.quickSort(intervals, 0, len(intervals) - 1, lambda x: x.start)
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            print('%s' % interval, end='')
        print()

        rst = []

        region_left = None
        region_right = None
        for t1 in intervals:
            if region_left is None:
                region_left = t1.start
                region_right = t1.end
                continue

            if region_right >= t1.start:
                region_right = max(region_right, t1.end)
            else:
                rst.append(Interval(region_left, region_right))
                region_left = t1.start
                region_right = t1.end
        if region_left is not None:
            rst.append(Interval(region_left, region_right))
        return rst

    def quickSort(self, lst, l, r, func):
        if l >= r:
            return

        key_idx = l
        key = lst[l]
        compare_key = func(lst[l])
        i, j = l, r
        while i < j:
            while func(lst[j]) >= compare_key and i < j:
                j -= 1
            if i < j:
                lst[key_idx] = lst[j]

            while func(lst[i]) <= compare_key and i < j:
                i += 1
            if i < j:
                lst[j] = lst[i]

            key_idx = i
        lst[key_idx] = key
        self.quickSort(lst, l, key_idx - 1, func)
        self.quickSort(lst, key_idx + 1, r, func)

    def quickSort2(self, lst, l, r):
        """
        :type lst: List[int]
        :rtype List[int]
        """
        if l < r:
            key = lst[l]
            i = l
            j = r
            while i < j:
                while lst[j] >= key and i < j:
                    j -= 1
                if i < j:
                    lst[i] = lst[j]

                while lst[i] <= key and i < j:
                    i += 1
                if i < j:
                    lst[j] = lst[i]
            lst[i] = key

            self.quickSort2(lst, l, i - 1)
            self.quickSort2(lst, i + 1, r)


if __name__ == "__main__":
    t = Solution()
    input_grid = [Interval(1, 3), Interval(8, 10), Interval(2, 6), Interval(15, 18)]
    t_result = t.merge(input_grid)
    for item in t_result:
        print('%s' % item, end='')

    # input_array = [2, 5, 33, 2, 17, 5, 2]
    # t.quickSort(input_array, 0, len(input_array) - 1, lambda x: x)
    # print(input_array)
    # input_array2 = [2, 5, 33, 2, 17, 5, 2]
    # t.quickSort2(input_array2, 0, len(input_array2) - 1)
    # print(input_array2)
