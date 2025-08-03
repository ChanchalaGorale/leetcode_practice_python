# Level: Easy
# Title: 2185. Counting Words With a Given Prefix
# Link: https://leetcode.com/problems/counting-words-with-a-given-prefix/

#Problem Summary:
#Given an array of strings words and a string pref, return the number of strings in words that start with the prefix pref.

from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for word in words:
            if word.startswith(pref):
                count+=1
        
        return count

#Time and Space Complexity:
#Where n is the number of words and L is the length of the prefix
#Time: O(n * L)
#Space: O(1)