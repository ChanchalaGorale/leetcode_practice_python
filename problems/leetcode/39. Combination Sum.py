
# Level: Medium
# Title: 39. Combination Sum
# Link: https://leetcode.com/problems/combination-sum

#Problem Summary:
#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.

# You may reuse the same number unlimited times.

# Note:

# All numbers are positive integers.

# The solution set must not contain duplicate combinations.

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i + 1 because we can reuse the same number
                path.pop()
        
        backtrack(0, [], 0)
        return res
    
#Time and Space Complexity:
#Time: O(2^T) where T = target.
#Space: 
# O(target) for recursion stack depth.
# O(k) per combination, total space for all combinations: O(#combos * k)