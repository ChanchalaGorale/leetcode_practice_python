
# Level: Medium
# Title: 15. 3Sum
# Link: https://leetcode.com/problems/3sum/

#Problem Summary:
#Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:
# i ≠ j ≠ k and nums[i] + nums[j] + nums[k] == 0
# Return the list of triplets, with no duplicates.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicate elements for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif two_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
        
    

#Time and Space Complexity:
#Time: O(n²) → Outer loop O(n) + inner loop O(n)
#Space: O(1) extra (ignoring output)