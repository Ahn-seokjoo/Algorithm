n, c = list(map(int,input().split()))

array = []
for _ in range(n):
  array.append(int(input()))
array.sort()
start = array[1]- array[0] # 좌표 가장 작은 gap
end = array[-1] - array[0] # 좌표 가장 큰 gap
result = 0

while(start <= end):
  mid = (start+ end) // 2
  value = array[0]
  count = 1

  for i in range(1,n):
    if array[i] >= value + mid: # 앞에서부터 설치
      value = array[i]
      count += 1
  if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우 거리를 늘린다
    start = mid + 1
    result = mid #최적의 결과를 저장
  else: # c개 이상의 공유기 설치가 안된다면 거리 감소
    end = mid -1

print(result)
      
