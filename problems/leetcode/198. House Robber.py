
# Level: Medium
# Title: 198. House Robber
# Link: https://leetcode.com/problems/house-robber

#Problem Summary:
#You are a professional robber planning to rob houses along a street. Each house has some amount of money stashed, and adjacent houses cannot be robbed on the same night (you will trigger the alarm).

# Given an integer array nums representing the amount of money at each house, return the maximum amount you can rob without alerting the police.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = 0  # dp[i-1]
        prev2 = 0  # dp[i-2]

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)