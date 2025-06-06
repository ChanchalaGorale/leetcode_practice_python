# Level: Medium
# Title: 916. Word Subsets
# Link: https://leetcode.com/problems/word-subsets/

#Problem Summary:
# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a at least as many times as in b.
# A string a from words1 is a universal word if for every b in words2, b is a subset of a.
# Return all universal words from words1.

from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            return Counter(word)

        # Step 1: Build the max frequency map from words2
        max_freq = Counter()
        for word in words2:
            freq = count(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])
        
        # Step 2: Check each word in words1
        result = []
        for word in words1:
            word_freq = count(word)
            if all(word_freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result

#Time and Space Complexity:
#n = len(words1), m = len(words2)
#Time: O((n + m) * 26) ≈ linear in number of words, since only 26 lowercase letters
#Space: O(26) for max_freq and word_freq per word ⇒ O(1) auxiliary space
