def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2 +1):
        compressed = ""
        prev = s[:step]
        count = 1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                count = 1
                prev = s[j:j+step]
        
        compressed += str(count) + prev if count >= 2 else prev # 나머지 처리, 3c는 만들었으나 붙여주는 코드가 없음. so 여기서 붙어줌
        
        answer = min(answer,len(compressed))
    return answer
