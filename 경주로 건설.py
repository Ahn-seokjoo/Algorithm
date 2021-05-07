from collections import deque
INF = int(1e9)

def solution(board):
    length = len(board)
    def bfs(start):
        table = [[INF]*length for _ in range(length)]
        dirs = [(-1,0),(0,-1),(1,0),(0,1)] #좌,위,우,아래
        
        q = deque([start])
        table[0][0] = 0
        while q:
            x,y,cost,dist = q.popleft()
            for idx,(dx,dy) in enumerate(dirs): # enum 이용해 인덱스도 같이 뽑아내서 방향까지 계산
                nx,ny = x + dx ,y + dy
                n_cost = cost + 600 if idx != dist else cost + 100
                
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0 and table[nx][ny] > n_cost:
                    table[nx][ny] = n_cost #테이블에는 값을 계속해서 저장
                    q.append((nx,ny,n_cost,idx))
        return table[-1][-1]
    return min(bfs((0,0,0,2)),bfs((0,0,0,3)))
