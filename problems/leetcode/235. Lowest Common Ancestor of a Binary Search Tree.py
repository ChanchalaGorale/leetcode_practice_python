
# Level: Medium
# Title: 235. Lowest Common Ancestor of a Binary Search Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

#Problem Summary:
#Given a Binary Search Tree (BST) and two node values p and q, return their Lowest Common Ancestor (LCA).

# The LCA of two nodes is the lowest node in the tree that has both p and q as descendants.

# BST property: Left < Root < Right

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # LCA must be in the left subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right  # LCA must be in the right subtree
            else:
                return root  # Split happens here → this is the LCA
    

#Time and Space Complexity:
#Time: O(log n) for balanced BST; O(n) worst case
#Space: O(1) (iterative) or O(h) (recursive)