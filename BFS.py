from collections import deque

def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue: #큐가 빌 떄까지
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]: #방문 안했다면
        queue.append(i) #큐에 다시 넣기
        visited[i] = True

graph= [[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]]

visited = [False] * 9
bfs(graph,1,visited)
