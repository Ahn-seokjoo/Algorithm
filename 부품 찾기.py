def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid # 리스트의 인덱스를 반환
	elif array[mid] > target: # 찾는 값이 중간 값보다 작은 경우
		return binary_search(array, target, start, mid -1) # 끝점을 중간 -1로 잡고, 다시 수행
	else :                    # 찾는 값이 중간 값보다 큰 경우
		return binary_search(array, target, mid+1, end)  # 시작 점을 중간 + 1로 잡고, 다시 수행
n = int(input())
# target = list(map(int,input().split())) #원소의 개수, 찾고자 하는 문자 입력
array = list(map(int,input().split()))
array.sort()
m = int(input())
x = list(map(int,input().split()))
#이진 탐색 수행
for i in x:
  result = binary_search(array,i,0,n-1)
  if result != None:
    print("yes",end = ' ')
  else:
    print("no", end = ' ')
    
   
