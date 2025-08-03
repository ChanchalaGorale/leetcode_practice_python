
# Level: Medium
# Title: 416. Partition Equal Subset Sum
# Link: https://leetcode.com/problems/partition-equal-subset-sum

#Problem Summary:
#Given an array nums, return True if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always possible

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

#Time and Space Complexity:
#Time: O(n * target)
#Space: O(target)