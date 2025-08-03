# Given a binary matrix (containing only 0s and 1s), count the total number of square submatrices that are filled with only 1s.

def countSquares(matrix):
  if not matrix:
    return 0
  
  rows, cols = len(matrix), len(matrix[0])
  dp=[[0]* cols for _ in range(rows)]
  total=0
  for i in range(rows):
    for j in range(cols):
      if matrix[i][j] ==1:
        if i ==0 or j==0:
          dp[i][j]=1
        else:
          dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        total+=dp[i][j]
  return total
