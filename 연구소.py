n, m = map(int,input().split())
temp =[[0]*m for _ in range(n)]
labaratory = []
result = 0

for _ in range(n):
  labaratory.append(list(map(int,input().split())))
# 전체를 확인해볼것 얼마 안걸림
# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 전염 함수(bfs)로 양옆위아래 0인경우 2로 감염 시킴
def virus(x,y):
  # 범위를 벗어나지 않으면서, 0인경우 2로 바꿈
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and ny >= 0 and nx < n and ny < m:
       if temp[nx][ny] == 0:
         temp[nx][ny] = 2
         virus(nx,ny)
# 전체 돌면서 확인 함수
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
        temp[i][j] = labaratory[i][j]
    # 각 바이러스 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
    result = max(result,get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if labaratory[i][j] == 0:
        labaratory[i][j] = 1
        count += 1
        dfs(count)
        labaratory[i][j] = 0
        count -= 1
dfs(0)
print(result)
