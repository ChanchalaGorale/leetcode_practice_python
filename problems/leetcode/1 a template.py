
# Level: Medium
# Title: 684. Redundant Connection
# Link: https://leetcode.com/problems/redundant-connection

#Problem Summary:
#You are given a graph that started as a tree with n nodes labeled 1 to n, and one extra edge added. The graph is now a cycle.

# Your task is to find the edge that can be removed so that the resulting graph is a tree.

# Return the edge that can be removed last in order if multiple answers exist.

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # cycle detected
            parent[rootY] = rootX
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
    

#Time and Space Complexity:
#Time: O(N * α(N))
#Space: O(N)