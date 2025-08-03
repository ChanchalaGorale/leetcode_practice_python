
# Level: Easy
# Title: 20. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses

#Problem Summary:
#Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.
#
# A string is valid if:
# Open brackets are closed by the same type of brackets.
# Open brackets are closed in the correct order.
# Every closing bracket has a corresponding open bracket of the same type.

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing brackets to opening ones
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack
    

#Time and Space Complexity:
#Time: O(n) — where n is the length of the string
#Space: O(n) — in the worst case (all open brackets), stack stores all characters