# Level: Easy
# Title: 3042. Count Prefix and Suffix Pairs I
# Link: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

#Problem Summary:
#Given a list of strings words, return the number of distinct pairs (i, j) such that: i < j, and words[i] is both a prefix and a suffix of words[j].

from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
    
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        
        return count

#Time and Space Complexity:
#n = number of words
#L = maximum length of any word in the list
#Time: O(n² * L)
#Space: O(1) (excluding input size)