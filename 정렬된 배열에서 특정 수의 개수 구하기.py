from bisect import bisect_left, bisect_right
# bisect_left, right는 left = left_value가 들어갈 인덱스를 구해준다
def count_by_range(array,left_value,right_value):
  left_value = bisect_left(array,left_value)
  right_value = bisect_right(array,right_value)
  return right_value - left_value
# left_value~right_value 의 개수를 리턴
n, m = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_range(array,m,m)

if count == 0:
  print(-1)
else:
  print(count)


