def count_subsets(nums, target):
  n=len(nums)

  dp = [[0] *(target+1) for _ in range(n+1)]

  for i in range(n+1):
    dp[i][0] = 1
  
  for i in range(1, n+1):
    for j in range(target + 1):
      if nums[i-1] <=j:
        dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
      else:
        dp[i][j] = dp[i-1][j]
  return dp[n][target]
