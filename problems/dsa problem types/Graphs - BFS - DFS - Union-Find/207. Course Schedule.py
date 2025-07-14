
# Level: Medium
# Title: 207. Course Schedule
# Link: https://leetcode.com/problems/course-schedule/

#Problem Summary:
#You are given numCourses courses labeled 0 to numCourses - 1, and a list of prerequisite pairs prerequisites, where each pair [a, b] indicates that to take course a, you must first take course b.

# Return True if it's possible to finish all courses, otherwise return False.

# This is a classic cycle detection problem in a directed graph.

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        # Build graph and indegree count
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # Queue of courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
    

#Time and Space Complexity:
#Time: O(V + E)
#Space: O(V + E)