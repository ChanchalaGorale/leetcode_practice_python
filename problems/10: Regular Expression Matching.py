
# Level: Hard
# Title: 10: Regular Expression Matching
# Link: https://leetcode.com/problems/regular-expression-matching/

#Problem Summary:
# Implement regular expression matching with support for '.' and '*'.
# '.' → Matches any single character.
# '*' → Matches zero or more of the preceding character.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                # Skip '*' + its preceding char OR use '*' once and continue
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)

#Time and Space Complexity:
#Time: O(len(s) × len(p)) 
#Space: O(len(s) × len(p)) 