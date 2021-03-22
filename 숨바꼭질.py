import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
#시작 노드를 1번으로 설정
start = 1
graph = [[] for i in range(n+1)]
#최단거리 테이블 초기화
distance =[INF] *(n+1)

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

def dijkstra(start):
  q = []

  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      #현재 노드를 거쳐 다른 노드 이동 거리가 더 짧을 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
dijkstra(start)
max_mode = 0
max_distance = 0
result = []

for i in range(1,n+1):
  if max_distance < distance[i]:
    max_node = i
    max_distance = distance[i]
    result = [max_node]
  elif max_distance == distance[i]:
    result.append(i)
print(max_node,max_distance,len(result))
