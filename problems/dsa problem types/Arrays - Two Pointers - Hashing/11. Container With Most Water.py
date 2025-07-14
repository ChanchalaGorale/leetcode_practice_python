
# Level: Medium
# Title: 11. Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water

#Problem Summary:
#You are given an array height of length n. Each element represents the height of a vertical line drawn at that index. The lines form a container with the x-axis. You need to find the maximum amount of water a container can store.

# The container is formed by choosing two lines. The amount of water is determined by the shorter of the two lines times the distance between them.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)