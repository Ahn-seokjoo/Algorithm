def solution(board, moves):
    answer = 0
    moves = [i-1 for i in moves]
    stack = []
    for target in moves:
        for i in range(len(board)):
            if board[i][target] != 0 :
                stack.append(board[i][target])
                board[i][target] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer
#1 = 퍼렁이 # [1,5,3,5,1,2,1,4]
#2 = 노랑이 # [4-3-1-1-3-2-3-4] => 1+1, 3+3
#3 = 초록이
#4 = 분홍이
#5 = 카톡개
