
# Level: Medium
# Title: 5. Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring

#Problem Summary:
#Given a string s, return the longest palindromic substring in s.

# A palindrome reads the same forward and backward.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # valid palindrome slice

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            p1 = expand_around_center(i, i)
            # Even-length palindrome
            p2 = expand_around_center(i, i + 1)

            # Update longest if needed
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest
        

#Time and Space Complexity:
#Time: O(n^2) — worst-case two pointers expand for each character.
#Space: O(1) — no extra space used (excluding output).