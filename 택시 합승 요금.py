INF = int(1e9)

def solution(n, s, a, b, fares):
    length = len(fares) #간선의 개수
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for q in range(1,n+1):
        for w in range(1,n+1):
            if q==w:
                graph[q][w] = 0
    
    for q,w,e in fares:
        graph[q][w] = e
        graph[w][q] = e

    for k in range(1,n+1):
        for q in range(1,n+1):
            for w in range(1,n+1):
                if(graph[q][w] > graph[q][k]+graph[k][w]):
                    graph[q][w] = graph[q][k]+graph[k][w]
    
    answer = int(INF)
    for i in range(1,n+1):
        answer =min(answer,graph[s][i]+graph[i][a]+graph[i][b])
        
    return answer
