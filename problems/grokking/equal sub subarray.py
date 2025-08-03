def hasEqualSumSubarrays(nums):
  n=len(nums)
  seen = set()

  for i in range(n):
    curr_sum=0
    for j in range(i, n):
      curr_sum+=nums[j]
      if (i, j) !=(0, n-1) and curr_sum in seen:
        return True
      seen.add(curr_sum)
  return False
