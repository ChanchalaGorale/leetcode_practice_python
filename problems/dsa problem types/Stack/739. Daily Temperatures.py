
# Level: Medium
# Title: 739. Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures

#Problem Summary:
#Given an array of integers temperatures representing the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.

# If there is no future day for which this is possible, set answer[i] = 0.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer
    

#Time and Space Complexity:
#Time: O(n)
#Space: O(n)