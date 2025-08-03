def isSubsetSum(nums, target):
  memo = {}

  def dfs(i, total):
    if total ==0:
      return True
    if i==len(nums) or total <0:
      return False
    if (i, total) in memo:
      return memo[(i, total)]
    
    include = dfs(i+1, total-nums[i])
    exclude = dfs(i+1, total)
    memo[(i, total)] = include or exclude
    
    return memo[(i, total)]
  
  return dfs(0, target)
