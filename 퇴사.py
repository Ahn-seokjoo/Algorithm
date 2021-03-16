n = int(input())

t = [] #상담 기간
p = [] #상담 금액
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
  x, y = map(int,input().split())
  t.append(x)
  p.append(y)

for i in range(n-1,-1,-1):
  time = t[i] + i
  if time <= n:
    dp[i] = max(p[i] + dp[time],max_value)
    max_value = dp[i]
  else:
    dp[i] = max_value

print(max_value)  

#뒤에서부터 확인하여 최고 이익 계산, 2회차때 더 자세히 볼 것
