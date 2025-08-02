
# Level: Medium
# Title: 416: Partition Equal Subset Sum
# Link: https://leetcode.com/problems/partition-equal-subset-sum

#Problem Summary:
#Given an integer array nums, return true if you can partition the array into two subsets such that the sum of elements in both subsets is equal, otherwise return false.

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False  

        target = total // 2
        n = len(nums)

        dp = [False] * (target + 1)
        dp[0] = True  

        for num in nums:
            for i in range(target, num - 1, -1):  
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

#Time and Space Complexity:
#Time: O(n * target)
#Space: O(target)
