
n = int(input())
store = list(map(int,input().split()))
m = int(input())
customer = list(map(int,input().split()))

array = [0] * (int(max(store)) + 1)

for i in store:
  array[i] = 1

for i in customer:
  if array[i] == 1:
    print("yes",end=' ')
  else:
    print("no",end=' ')
