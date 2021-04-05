n, m = map(int,input().split())
x,y,direction = map(int,input().split())
d = [[0] *m for _ in range(n)]
d[x][y] = 1
array = []
for _ in range(n):
  array.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
turn_count = 0
result = 1 # 이미 시작부터 한칸 밟고 있기 때문에 1부터 시작
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    result += 1
    turn_count = 0
    continue
  else:
    turn_count += 1
  if turn_count == 4: # 문제 요구처럼네방향 모두 가본 칸이라면 바라본 방향 유지하며 다시 뒤로 한칸
    nx = x - dx[direction]
    ny = y - dy[direction]
    if array[nx][ny] == 0: # 뒤로 설정한 칸이 갈 수 있는 곳(0) 이라면 이동
      x = nx
      y = ny
    else:
      break
    turn_count = 0
      
print(result)
