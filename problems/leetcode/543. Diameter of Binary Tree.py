
# Level: Easy
# Title: 543. Diameter of Binary Tree
# Link: https://leetcode.com/problems/diameter-of-binary-tree

#Problem Summary:
#Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter is the length of the longest path between any two nodes in the tree.

# This path may or may not pass through the root.

# The length is the number of edges on the path (not nodes!).

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # update diameter at this node
            diameter = max(diameter, left + right)
            
            # return height to parent
            return 1 + max(left, right)

        dfs(root)
        return diameter
    

#Time and Space Complexity:
#Time: O(n) — each node is visited once.
#Space: O(h) — recursion stack; h is the height of the tree (worst case O(n)).