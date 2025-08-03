
# Level: Easy
# Title: 70. Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs

#Problem Summary:
#You are climbing a staircase. It takes n steps to reach the top.
# Each time, you can climb either 1 or 2 steps.
# Return the number of distinct ways to climb to the top.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2  # f(1), f(2)

        for _ in range(3, n + 1):
            first, second = second, first + second

        return second
    

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)