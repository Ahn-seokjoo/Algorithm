input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 ## 숫자행렬로 만들어줌 

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향으로 각위치로 이동이 가능한지
result = 0
for step in steps:
  next_row = row + step[0]            #행과 열에
  next_column = column + step[1]      #움직일수 있는 값들 더해준다
  #print(next_row, next_column)
  if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
    result += 1                       # 8x8 나갈 경우 안더해줌
print(result)


###2회차

n = input()
row = int(n[1])
column = int(ord(n[0]))-int(ord('a')) + 1
count = 0

move_type = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

for move in move_type:
  can_move_row = row + move[0]
  can_move_column = column + move[1]
  if 0 < can_move_row < 9 and 0 < can_move_column < 9:
    count += 1

print(count)
