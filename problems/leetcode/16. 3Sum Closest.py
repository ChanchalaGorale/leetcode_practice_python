
# Level: Medium
# Title: 16. 3Sum Closest
# Link: https://leetcode.com/problems/3sum-closest

#Problem Summary:
#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)

        for i in range(n-2):
            left = i+1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(target-current_sum) < abs(target-closest_sum):
                    closest_sum = current_sum
                if current_sum <target:
                    left+=1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum
    

#Time and Space Complexity:
#Time: O(n²)
#Space: O(1) 