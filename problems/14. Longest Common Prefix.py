
# Level: Easy
# Title: 14. Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/

#Problem Summary:
# Write a function to find the longest common prefix string among an array of strings.
# If there is no common prefix, return "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
        return strs[0]
        
    

#Time and Space Complexity:
#Time: O(S)
#Space: O(1)