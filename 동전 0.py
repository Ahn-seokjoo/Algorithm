n,m = map(int,input().split())
money = []
result =0
index = n-1
for i in range(n):
    money.append(int(input()))
for idx in range(index,-1,-1):
    if money[idx] < m:
        index = idx
        
        break
while m>0:
    if m >= money[index]:
        result += m// money[index]
        m %= money[index]
        index -= 1
    else:
        index -= 1
        if index == -1:
            break
print(result)
