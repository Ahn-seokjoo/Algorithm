def solution(n, costs):
    answer = 0
    v = n
    parent = [0] * (v+1)
    edges = []
    for i in range(1,v+1):
        parent[i] = i
    
    edges = sorted(costs,key= lambda x:x[2])
    for edge in edges:
        a, b, cost = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            answer += cost
    return answer

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a< b :
        parent[b] = a
    else:
        parent[a] = b
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
