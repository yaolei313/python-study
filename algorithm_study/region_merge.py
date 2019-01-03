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

        lst = []
        for i in range(len(intervals)):
            lst.append((intervals[i].start, i))
            lst.append((intervals[i].end, i))

        print(lst)

        self.quickSort(lst, 0, len(lst) - 1, lambda x: x[0])

        print(lst)

        rst = []

        # 处理中region集合
        region_no_set = set()
        for i in range(len(lst)):
            if len(region_no_set) == 0:
                region_no_set.add(i)
                region_left = lst[i][0]
                continue

            cur_region_no = lst[i][1]
            if cur_region_no in region_no_set:
                if len(region_no_set) == 1:
                    region_right = lst[i][0]
                    rst.append(Interval(region_left, region_right))
                else:
                    region_no_set.remove(cur_region_no)
            else:
                region_no_set.add(cur_region_no)
        return rst

    def quickSort(self, lst, l, r, func):
        if l >= r:
            return

        key_idx = l
        key = func(lst[l])
        i, j = l, r
        while i < j:
            while func(lst[j]) >= key and i < j:
                j -= 1
            if i < j:
                lst[key_idx] = lst[j]

            while func(lst[i]) <= key and i < j:
                i += 1
            if i < j:
                lst[j] = lst[i]

            key_idx = i
        lst[key_idx] = lst[l]
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
    input_grid = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    t_result = t.merge(input_grid)
    print(t_result)

    # input_array = [2, 5, 33, 2, 17, 5, 2]
    # t.quickSort(input_array, 0, len(input_array) - 1, lambda x: x)
    # print(input_array)
    # input_array2 = [2, 5, 33, 2, 17, 5, 2]
    # t.quickSort2(input_array2, 0, len(input_array2) - 1)
    # print(input_array2)
