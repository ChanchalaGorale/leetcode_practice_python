
# Level: Medium
# Title: 22. Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses

#Problem Summary:
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
    
#Time and Space Complexity:
#Time: O(4**n/sqrt(n))
#Space: O((4**n/sqrt(n))*n)
