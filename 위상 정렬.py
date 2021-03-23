from collections import deque

v, e = map(int,input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 입력
graph = [[] for i in range(v+1)]

for _ in range(e):
  a,b = map(int,input().split())
  graph[a].append(b)
  #진입 차수 1 증가
  indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
  result = []
  q = deque()

  #시작은 진입차수가 0인 노드를 큐에 삽입
  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      #새롭게 진입차수가 0이 되는 것은 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  # 위상정렬 결과 출력
  for i in result:
    print(i,end=' ')
    
topology_sort()
  
