def solution(gems):
    answer = []
    shortest = len(gems) + 1
    len_check = len(set(gems))
    dict = {}
    
    start = 0
    end = 0
    
    while end < len(gems):
        if gems[end] not in dict:
            dict[gems[end]] = 1
        else:
            dict[gems[end]] += 1
        end += 1
        
        if len_check == len(dict): # 다 들어갔을 때
            while start < end:
                if dict[gems[start]] > 1:
                    dict[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start+1,end]
                    break
                else:
                    break    
    return answer
