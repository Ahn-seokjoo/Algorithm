def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: #설치된 것이 기둥이라면
            #바닥 위 혹은 보의 한쪽 끝 또는 다른 기둥 위라면 가능
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1: #설치된 것이 보라면
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True
            
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0: #삭제하는 경우
            answer.remove([x,y,stuff]) # 일단 삭제 해본 뒤
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x,y,stuff]) #가능하다면 다시 설치
        if operate == 1:
            answer.append([x,y,stuff]) #일단 설치 해본 뒤
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)
                
