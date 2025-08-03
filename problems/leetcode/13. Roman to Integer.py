
# Level: Easy
# Title: 13. Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/

#Problem Summary:
# Convert a Roman numeral string s to an integer.
# Roman numeral rules:
# Roman numerals are usually written from largest to smallest left to right.
# But, if a smaller symbol comes before a larger one, it means subtraction:
# IV = 4, IX = 9, XL = 40, CM = 900, etc.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        prev = 0

        for char in reversed(s):
            value = roman[char]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)