INF = int(1e9)
n, m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n + 1)]

#자신 > 자신 0으로
for a in range(n+1):
  for b in range(n+1):
    if a == b:
      graph[a][b] = 0

#연결 도로 입력
for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int,input().split())
#플로이드 워셜 이용한 초기화
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >=INF:
  print("-1")
else:
  print(distance)
