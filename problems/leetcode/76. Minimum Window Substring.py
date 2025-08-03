
# Level: Hard
# Title: 76. Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring

#Problem Summary:
#Given two strings s and t, return the minimum window in s which will contain all the characters in t (including duplicates).
# If there is no such window, return the empty string "".

from typing import List

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)

        res = [float("inf"), 0, 0]  # [window length, left, right]
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                # Update result if this window is smaller
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left, right]

                # Pop from the left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res[1], res[2]
        return s[l:r+1] if res[0] != float("inf") else ""
    

#Time and Space Complexity:
#Time: O(s + t)
#Space: O(s + t)