
# Level: Medium
# Title: 133. Clone Graph
# Link: https://leetcode.com/problems/clone-graph/

#Problem Summary:
#Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

# Each node has a value and a list of neighbors.

from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]
            
            clone = Node(n.val)
            visited[n] = clone
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
        
    

#Time and Space Complexity:
#Time: O(N + E)
#Space: O(N) > N: number of nodes