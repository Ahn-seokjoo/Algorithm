n,c = list(map(int,input().split(' ')))
array = []
for _ in range(n):
  array.append(int(input()))
array.sort()

start = array[1]- array[0] # 집의 좌표 중 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중 가장 큰 값
result = 0

while(start<=end):
  mid = (start + end) // 2 # mid 는 인접한 두 공유기 사이의 거리를 의미한다
  value = array[0]
  count = 1
  # mid 값을 이용해 공유기 설치
  for i in range(1,n):
    if array[i] >= value + mid :
      value = array[i]
      count += 1
  if count >= c: # c개 이상 설치가 가능하면 거리를 늘려본다
    start = mid + 1
    result = mid
  else:
    end = mid - 1
print(result)
