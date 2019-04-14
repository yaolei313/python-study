#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        result = []

        node_queue = []
        cur_level = 1
        cur_lst = []
        node_queue.append((1, root))
        while len(node_queue) != 0:
            level, node = node_queue.pop(0)
            if cur_level == level:
                cur_lst.append(node.val)
            else:
                result.append(cur_lst)
                cur_level = level
                cur_lst = [node.val]

            if node.left is not None:
                node_queue.append((level + 1, node.left))
            if node.right is not None:
                node_queue.append((level + 1, node.right))

        result.append(cur_lst)
        result.reverse()

        return result


if __name__ == "__main__":
    t = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    rst = t.levelOrderBottom(root)
    print("{}".format(rst))
