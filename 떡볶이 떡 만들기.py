n, m = map(int,input().split())
array = list(map(int,input().split()))

#시작점 끝점 설정
start = 0
end = max(array)

#이진 탐색 수행
result = 0
while(start<=end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    # 잘랐을 때의 떡의 양 계산
    if x > mid:
      total += x - mid
  # 자른 떡이 부족한경우 더 많이 자르기
  if total < m:
    end = mid - 1
  # 충분한 경우 덜 자르기
  else:
    result = mid #최대한 덜자른 것이 정답
    start = mid + 1
print(result)
