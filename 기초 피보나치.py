def fibo(x):
  if x == 1 or x == 2 :
    return 1
  return fibo(x - 1 ) + fibo (x - 2)

print(fibo(4))

# 이런 식으로 작성시에는 n이 커질수록 수행 시간이 기하급수적으로 늘어난다.
# n = 30의 경우 10억 가량의 연산을 해야하므로 추천되지 않는다
