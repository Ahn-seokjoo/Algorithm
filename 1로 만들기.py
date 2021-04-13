n = int(input())
d = [0] * (30001)

for i in range(2,n+1):
  d[i] = d[i-1] + 1 # 이코드를 통해 d[i] = min(d[i],d[i//x]) 가성립하는데,
  #이전 수에서 1을 뺀 값과 d[i//x]를 비교하여 더 값이 작은 것으로 dp테이블을 초기해주는 것이다
  if d[i] % 2 == 0:
    d[i] = min(d[i],d[i//2]+1)
  if d[i] % 3 == 0:
    d[i] = min(d[i],d[i//3]+1)
  if d[i] % 5 == 0:
    d[i] = min(d[i],d[i//5]+1)
print(d[n])
