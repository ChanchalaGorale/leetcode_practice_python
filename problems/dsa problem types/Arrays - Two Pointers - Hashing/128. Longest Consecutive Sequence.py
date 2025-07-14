
# Level: Medium
# Title: 128. Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence

#Problem Summary:
#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # only start counting if it's the start of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

#Time and Space Complexity:
#Time: O(n)
#Space: O(n)