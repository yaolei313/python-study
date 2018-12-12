#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        inc = 0
        current_l1 = l1
        current_l2 = l2

        dummy_head = ListNode(0)
        current_node = dummy_head

        while current_l1 or current_l2:
            value = inc
            if current_l1:
                value += current_l1.val
                current_l1 = current_l1.next
            if current_l2:
                value += current_l2.val
                current_l2 = current_l2.next
            if value >= 10:
                current_node.next = ListNode(value - 10)
                inc = 1
            else:
                current_node.next = ListNode(value)
                inc = 0
            current_node = current_node.next

        if inc:
            current_node.next = ListNode(inc)

        return dummy_head.next


if __name__ == "__main__":
    sol = Solution()
    lst1 = ListNode(2)
    lst1.next = ListNode(4)
    lst1.next.next = ListNode(3)

    lst2 = ListNode(5)
    lst2.next = ListNode(6)
    # lst2.next.next = ListNode(4)

    output_array = sol.addTwoNumbers(lst1, lst2)
    print(output_array)
