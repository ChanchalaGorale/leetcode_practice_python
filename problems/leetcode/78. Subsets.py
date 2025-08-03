
# Level: Medium
# Title: 78. Subsets
# Link: https://leetcode.com/problems/subsets

#Problem Summary:
#Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution must not contain duplicate subsets. Return the answer in any order.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # start with the empty subset
        for num in nums:
            # For each existing subset, add a new subset that includes num
            result += [curr + [num] for curr in result]
        return result
    

#Time and Space Complexity:
#Time: O(2^n) — There are 2^n subsets for n elements.
#Space: O(2^n * n) — Each subset can be up to n elements long.