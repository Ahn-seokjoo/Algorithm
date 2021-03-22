def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a= find_parent(parent,a)
  b= find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

v, e =map(int,input().split())
parent = [0] * (v+1)

edges = []
result = 0
#부모를 자기 자신으로 초기화
for i in range(1,v+1):
  parent[i] = i
#간선 정보 입력받기
for _ in range(e):
  a, b, cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()
# 간선 확인하며
for edge in edges:
  cost,a,b = edge
  # 사이클 발생 안할 때 집합에 포함
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost
print(result)
