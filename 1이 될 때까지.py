n, k = map(int,input().split())
result = 0

while(True):
  target = (n//k) * k
  result += (n- target)
  n = target
  if n< k:
    break;
  result += 1
  n //= k

# 이때 n =0 이라 (n-1)을 더해주면 1을 빼주게 되는 것이고, 이는 다 나눈 뒤 1이 되었을때 한번 더해주기 때문에 1을 다시 빼주는 것이다
result += (n-1)
print(result)
    
