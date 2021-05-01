from collections import deque

n, k = map(int,input().split())
graph = []
data= []
for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j],0,i,j))

data.sort()
q = deque(data)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ts,tx,ty = map(int,input().split())
while q:
  virus,s,x,y = q.popleft()
  if s == ts:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and ny >= 0 and nx < n and ny < n :
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus,s+1,nx,ny))
print(graph[tx-1][ty-1])

