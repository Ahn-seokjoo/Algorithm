INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j] = 0

for _ in range(m):
  x,y,z = map(int,input().split())
  if z < graph[x][y]: # 짧은 곳만 저장
    graph[x][y] = z


for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] != INF:
      print(graph[i][j],end=' ')
    else:
      print(0,end=" ")
  print()
