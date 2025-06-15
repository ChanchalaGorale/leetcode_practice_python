
# Level: Easy
# Title: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/

#Problem Summary:
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(nums, target):
        num_map = {}  # To store number: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

#Time and Space Complexity:
#Time: O(n)
#Space: O(n) 