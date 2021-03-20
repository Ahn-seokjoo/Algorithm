import sys
import heapq
input = sys.stdin.readline
INF = 1e9
# 노드의 수, 간선의 개수 입력
n , m = map(int,input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph =[[] for i in range(n + 1)]
# 방문한 적 잇는지에 대해 체크
visited = [False] * (n + 1)
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
  a,b,c = map(int,input().split())
  #a번 노드에서 b번 노드로 가는 비용 = c
  graph[a].append((b,c))


def dijkstra(start):
  # 시작 노드 초기화
  q = []
  #시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    # 처리 됐다면 무시
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      # 다른 노드로 이동 거리가 더 짧다면
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))


dijkstra(start)
for i in range(1, n + 1):
  # 도달할 수 없는 경우, 무한(INF)을 출력
  if distance[i] == INF:
    print("INF")
  # 도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])
