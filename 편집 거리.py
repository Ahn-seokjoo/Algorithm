def edit_dist(str1,str2):
  n = len(str1)
  m = len(str2)

  dp = [[0] * (m+1) for _ in range(n+1)]

  for i in range(1,n+1):
    dp[i][0] = i
  for j in range(1,m+1):
    dp[0][j] = j
  
  #최소 편집거리 계산
  for i in range(1,n+1):
    for j in range(1,m+1):
      #문자가 같다면 왼쪽 위 숫자 대입
      if str1[i-1] == str2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      #문자가 다르면 3가지 중에서 최솟값 찾기
      else:
        dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
  return dp[n][m]
str1 = input()
str2 = input()
print(edit_dist(str1,str2))
