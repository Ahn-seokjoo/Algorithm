import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 개수, 간선의 개수
n, m = map(int,input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 노드 정보 담기
graph = [[] for i in range(n+1)]
# 최단거리 테이블 일단 무한으로 초기화
distance = [INF] *(n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0  #자신으로 가는 거리 0
  while q:
    # 최단거리 짧은거 빼기
    dist, now = heapq.heappop(q)
    # 현재의 노드가 이미 처리 됐다면 무시
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      # 현재노드 거쳐서 다른 노드로 가는게 더 작으면
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
