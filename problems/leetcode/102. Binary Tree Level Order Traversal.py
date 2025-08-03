
# Level: Medium
# Title: 102. Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal

#Problem Summary:
#Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result

#Time and Space Complexity:
#Time: O(n) — every node is visited once.
#Space: O(n) — for the queue and result list.