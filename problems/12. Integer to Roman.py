
# Level: Medium
# Title: 12. Integer to Roman
# Link: https://leetcode.com/problems/integer-to-roman/

#Problem Summary:
# Convert an integer to a Roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:
        val_to_roman = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        res = ""
        for val, symbol in val_to_roman:
            while num >= val:
                res += symbol
                num -= val
        return res

#Time and Space Complexity:
#Time: O(1)
#Space: O(1)