//이진 탐색, 파라메트릭 서치!
n, m = list(map(int,input().split(' ')))

array = list(map(int,input().split()))

start = 0 
end = max(array)

result=0
while(start<=end):
  total = 0
  mid = (start + end) //2

  for x in array:
    if x>mid:
      total += x - mid
    
  if total < m:
    end = mid-1
  else:
    result = mid
    start = mid + 1

print(result)

#### 2회 풀이

n, m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

start = 0 
end = max(array)

result = 0
while(start<=end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      #잘랐을 때의 양 = x - mid 을 total에 더해주어 총 자른 양을 구함
      total += x - mid
  if total < m:
    #떡의 양이 적으면 왼쪽을 늘려 떡의 길이를 늘려준다
    end = mid -1
  else:
    #충분한 경우 오른쪽에서 덜 자르기
    result = mid #최대한 덜 잘랐을 때가 정답, 
    start = mid + 1
print(result)
