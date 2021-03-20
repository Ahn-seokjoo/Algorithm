INF = int(1e9)

#노드 및 간선의 수
n = int(input())
m = int(input())

# 2차원 그래프를 만든 뒤 모두 inf로 초기화
graph =[[INF]*(n+1) for _ in range(n+1)]
# 자신에게 가는 비용은 모두 0
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b] = 0

for _ in range(m):
  #간선 정보 받기
  a,b,c = map(int,input().split())
  graph[a][b] = c

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("INF", end=" ")
    else:
      print(graph[a][b],end=" ")
  print()
