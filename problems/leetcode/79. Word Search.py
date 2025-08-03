
# Level: Medium
# Title: 79. Word Search
# Link: http://leetcode.com/problems/word-search

#Problem Summary:
#Given an m x n 2D board of characters and a string word, return true if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where “adjacent” cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'  # mark as visited

            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            board[r][c] = temp  # backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
    

#Time and Space Complexity:
#Time: O(m * n * 4^L)
# > m * n: each cell is a potential start.
# > 4^L: at each step, 4 directions tried (L = length of word).
#Space: O(L) recursion stack for DFS (L = length of word).