
# Level: Medium
# Title: 18. 4Sum
# Link: https://leetcode.com/problems/4sum

#Problem Summary:
#Given an array nums of n integers and an integer target, return all unique quadruplets [a, b, c, d] such that: a+b+c+d =target

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort to use two pointers and handle duplicates
        n = len(nums)
        res = []

        for i in range(n - 3):
            # Skip duplicate a's
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early pruning
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicate b's
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Early pruning
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                
                # Two-pointer search for c + d = target - (a + b)
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return res
    

#Time and Space Complexity:
#Time: O(n³)
#Space: O(1)