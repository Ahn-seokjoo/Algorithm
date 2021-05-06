from collections import deque
INF = int(1e9)

def solution(board):
    length = len(board)
    def bfs(start):
        table = [[INF] * length for _ in range(length)]
        
        dirs= [(-1,0),(0,-1),(1,0),(0,1)]
        queue = deque([start])
        
        table[0][0] = 0
        while queue:
            y,x,cost,head = queue.popleft()
            for idx,(dy,dx) in enumerate(dirs):
                ny ,nx = y+dy ,x+dx
                
                n_cost = cost + 600 if idx != head else cost + 100
                
                if 0 <= ny < length and 0 <= nx < length and board[ny][nx] == 0 and table[ny][nx] > n_cost:
                    table[ny][nx] = n_cost
                    queue.append((ny,nx,n_cost,idx))
        return table[-1][-1]
    return min(bfs((0,0,0,2)),bfs((0,0,0,3)))
