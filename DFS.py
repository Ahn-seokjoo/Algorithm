def dfs(graph,v,visted):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited) # 재귀적으로 호출

graph = [[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]]
visited = [False] * 9 # 처음은 False
dfs(graph,1,visited) # 1 부터 시작
