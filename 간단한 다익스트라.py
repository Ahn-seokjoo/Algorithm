import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
# 각 노드에 연결되어 있는 정보를 담는 리스트 
graph = [[]for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [0] *(n+1)
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 그래프 값 넣기
for _ in range(m):
  a,b,c = map(int,input().split())
  #a에서 b가는 비용 c
  graph[a].append((b,c))

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  for i in range(n-1):
    #현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리
    now = get_smallest_node()
    visited[now] = True
    #현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
    

