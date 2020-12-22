array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end

  while left<=right: 
    #피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]: 
      left += 1 
    #피벗보다 작은 데이터를 찾을 때 까지 반복
    while right > start and array[right] >= array[pivot]: 
      right -= 1 
    if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체 
      array[right], array[pivot] = array[pivot], array[right]
    else: # 아니라면 작은 데이터와 큰 데이터를 교체
      array[left],array[right] = array[right],array[left]
  #분할 뒤에 왼쪽, 오른쪽 각각 정렬
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)
quick_sort(array,0,len(array)-1)
print(array)

####파이썬의 장점을 살린 퀵정렬
#리스트 컴프리헨션 통해 정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  #리스트가 한개 남을시에 종료
  if len(array) <= 1:
    return array;
  pivot = array[0] #피벗은 시작시에는 첫 원소
  tail = array[1:] #첫번째 원소 이후의 원소

  ###리스트 컴프리헨션을 통해서 나눔 피벗보다 큰수와 작은수로
  left_side = [x for x in tail if x <=pivot]
  right_side = [x for x in tail if x > pivot]
  
  return quick_sort(left_side) +[pivot] +quick_sort(right_side)
  
print(quick_sort(array))
