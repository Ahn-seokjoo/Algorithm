#전체 벽을 세우고 max 값을 갱신해나가며 모든걸 해봄
#4방향으로 나아가는 bfs를 
#1. 벽세우기
#2. 개수 체크
#3. 바이러스 퍼지게하기 함수 구현
n, m = map(int,input().split())
graph = []
temp = [[0]*m for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0

def virus(x,y):
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if nx>=0 and ny >= 0 and nx <n and ny< m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx,ny)
        
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

def dfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = graph[i][j]
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
    result = max(result,get_score())
    return
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        count += 1
        dfs(count)
        graph[i][j] = 0
        count -= 1
dfs(0)
print(result) 
