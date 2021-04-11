#####스택과 큐는 dfs,bfs 문제에서 필수 기초이므로 짚고 넘어감####
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(4)

print(stack)#최하단부터(맨앞부터) 출력
print(stack[::-1])# 최상단부터 출력

###[1,2,4]
###[4,2,1]
###스택은 일반 리스트와 동일하게 사용

from collections import deque

queue = deque()
#deque 라이브러리를 이용하여 queue를 큐로 이용
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력
###deque([3,7,1,4])
###deque([4,1,7,3])
