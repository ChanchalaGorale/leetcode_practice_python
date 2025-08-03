
# Level: Medium
# Title: 7: Reverse Integer.
# Link: https://leetcode.com/problems/reverse-integer/

#Problem Summary:
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], return 0.

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_str = str(x_abs)[::-1]
        reversed_int = sign * int(reversed_str)

        # Clamp to 32-bit signed integer range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        return reversed_int
    

#Time and Space Complexity:
#Time: O(log₁₀(n))
#Space: O(log₁₀(n))