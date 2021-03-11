from bisect import bisect_left, bisect_right

n, x = map(int,input().split())

array = list(map(int,input().split()))

def found(array,left,right):
  left_index = bisect_left(array,left)
  right_index = bisect_right(array,right)
  return right_index - left_index

count = found(array,m,m)
if count != 0:
  print(count)
else:
  print("-1")
