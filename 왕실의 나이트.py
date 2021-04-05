n = input()
y = int(n[1])
x = int(ord(n[0]) - ord('a')) + 1

move_type = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
count = 0
for i in move_type:
  nx = x + i[0]
  ny = y + i[1]
  if nx < 1 or ny <1 or nx >8 or ny > 8:
    continue
  count += 1
  
print(count)
