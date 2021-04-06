n = input()
result = []
value = 0

for x in n:
  if(x.isalpha()):
    result.append(x)
  else:
    value += int(x)

result.sort()
if value != 0: #하나라도 존재하면 뒤에 String 으로 붙임
  result.append(str(value))
print(''.join(result)) #문자열로 변환
  
