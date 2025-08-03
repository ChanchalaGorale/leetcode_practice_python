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
