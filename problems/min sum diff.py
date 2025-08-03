def minSubsetSumDifference(nums):
  total_sum = sum(nums)
  n=len(nums)
  target = total_sum//2
  dp=[False]*(target+1)
  dp[0]=True
  for num in nums:
    for j in range(target, num-1, -1):
      dp[j]= dp[j] or dp[j-num]
  
  for j in range(target, -1, -1):
    if dp[j]:
      s1=j
      break
  s2 = total_sum -s1

  return abs(s2-s1)
  
