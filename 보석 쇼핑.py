def solution(gems):
    answer = []
    dict = {} # 현재 구간에 포함된 보석들
    shortest = len(gems) + 1 # 현재 최단 구간 길이
    
    len_check = len(set(gems))
    start,end = 0,0 # 시작, 끝점
    
    while end < len(gems):
        if gems[end] not in dict: # 끝점의 보석이 없다면 추가
            dict[gems[end]] = 1
        else:
            dict[gems[end]] += 1
        end += 1 #끝점 증가
        
        if len(dict) == len_check: # 다 들어가 있다면
            while start < end: #start 가 end 보다 같을떄까지 증가
                if dict[gems[start]] > 1: # 보석 하나씩 빼보기
                    dict[gems[start]] -= 1
                    start += 1
                elif shortest > end - start: # 기존의 구간 최단거리보다 짧다면
                    shortest = end - start
                    answer = [start + 1,end] #답과 최단거리 갱신
                    break
                else:
                    break

    return answer
