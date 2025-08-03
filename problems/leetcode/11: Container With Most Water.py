
# Level: Medium
# Title: 11: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/

#Problem Summary:
#You are given an integer array height of length n.
# Each element represents the height of a vertical line drawn at that index.
# Find two lines that together with the x-axis form a container that holds the most water.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate area
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            # Move the shorter line inward (greedy)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
    

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)