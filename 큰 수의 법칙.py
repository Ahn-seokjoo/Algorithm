n,m,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort(reverse=True)
result = 0

first = array[0]
second = array[1]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count) * first
result += (m-count) * second
print(result)
