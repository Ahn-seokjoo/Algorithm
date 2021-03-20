# 도시 개수 n, 통로개수 m, 메시지를 보내고픈 도시 start
import sys
import heapq
input = sys.stdin.readline

n,m,start = map(int,input().split())

graph = [[] for i in range(n+1)]
INF = int(1e9)
distance = [INF]* (n+1)

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

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
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)
# 도달 가능한 노드 수
count = 0
# 도달 가능한 노드 중 가장 먼 노드와의 최단 거리
max_distance = 0

for d in distance:
  if d!= INF:
    count += 1
    max_distance = max(max_distance,d)

# 시작 노드 제외해야 해서 -1 해준다
print(count-1,max_distance)

    

