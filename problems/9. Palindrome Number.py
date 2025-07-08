
# Level: Easy
# Title: 9. Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/

#Problem Summary:
# Given an integer x, return True if x is a palindrome, and False otherwise. A palindrome number reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # For even digit count → x == reversed_half
        # For odd digit count → x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
    

#Time and Space Complexity:
#Time: O(log₁₀(x)) 
#Space: O(1)