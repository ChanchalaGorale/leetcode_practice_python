
# Level: Medium
# Title: 8. String to Integer (atoi)
# Link: https://leetcode.com/problems/string-to-integer-atoi/

#Problem Summary:
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi).

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. Remove leading whitespaces
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # 2. Check for overflow
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            num = num * 10 + digit
            i += 1

        return sign * num
        

#Time and Space Complexity:
#Time: O(n)
#Space: O(1)