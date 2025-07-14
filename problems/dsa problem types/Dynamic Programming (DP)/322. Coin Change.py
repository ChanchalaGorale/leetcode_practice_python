
# Level: Medium
# Title: 322. Coin Change
# Link: https://leetcode.com/problems/coin-change

#Problem Summary:
#You are given an integer array coins representing coin denominations and an integer amount.
# Return the fewest number of coins needed to make up that amount.
# If it's not possible, return -1.

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with a value greater than any possible solution
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
        
#Time and Space Complexity:
#Time: O(amount * len(coins))
#Space: O(amount)