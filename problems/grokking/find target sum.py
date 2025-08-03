def findTargetSum(nums, target):
  memo = {}

  def backtrack(index, total):
    if index == len(nums):
      return i if total == target else 0
    if (index, total) in memo:
      return memo[(index, total)]
      
    add = backtrack(index+1, total+nums[index])

    subtract = backtrack(index+1, total-nums[index])
    
    memo[(index, total)] = add+subtract

    return memo[(index, total)]

  return backtrack(0,0)


# Bottom-Up DP (Subset Sum Transformation)
def findTargetSumWays(nums, target):
    total = sum(nums)
    if (total + target) % 2 != 0 or total < abs(target):
        return 0
    subset_sum = (total + target) // 2

    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # one way to make sum 0

    for num in nums:
        for j in range(subset_sum, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[subset_sum]

