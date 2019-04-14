#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.maxDepth(root.right) + 1
        elif root.right is None:
            return self.maxDepth(root.left) + 1
        else:
            return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

    def maxDepthByDFS(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while len(stack) != 0:
            cur_depth, node = stack.pop()
            depth = max(depth, cur_depth)
            if node.left is not None:
                stack.append((cur_depth+1, node.left))
            if node.right is not None:
                stack.append((cur_depth+1, node.right))
        return depth


if __name__ == "__main__":
    sol = Solution()