
# Level: Medium
# Title: 17. Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number

#Problem Summary:
#Given a string of digits digits (2‑9) that maps to letters on a phone keypad, return all possible letter combinations the number could represent, in lexicographic order.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGIT_TO_CHARS: dict[str, str] = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        if not digits:
            return []

        res: list[str] = []

        def dfs(idx: int, path: list[str]) -> None:
            """Back–tracking over digit positions."""
            # base‑case: built one full combination
            if idx == len(digits):
                res.append("".join(path))
                return

            for ch in DIGIT_TO_CHARS[digits[idx]]:
                path.append(ch)        # choose
                dfs(idx + 1, path)     # explore
                path.pop()             # un‑choose (back‑track)

        dfs(0, [])
        return res
        
    

#Time and Space Complexity:
#Time: O(4ⁿ)
#Space: O(n)