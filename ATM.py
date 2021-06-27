n = int(input())
data = list(map(int,input().split()))
result = 0

data.sort()

for i in range(1,n+1):
  for j in range(0,i):
    result += data[j]
print(result)
