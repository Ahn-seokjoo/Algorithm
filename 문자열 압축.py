def solution(s):
    answer = len(s)
    # 1개 단위부터 늘려가며 확인, 중간까지
    for step in range(1,len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        #남은 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        #만들어지는 것들 중 가장 짧은 것이 정답
        answer = min(answer,len(compressed))
    
    return answer
