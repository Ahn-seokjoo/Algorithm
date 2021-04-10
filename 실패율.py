def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1,N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i,fail))
        length -= count
        
    answer = sorted(answer,key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

def solution(N, stages):
    answer=[]
    failure = []
    new_answer = []
    count = [0] *(N + 2)
    length = len(stages)
    
    for i in range(len(stages)):
        count[stages[i]] += 1
    
    for i in range(1,len(count)):
        if count[i] != 0:
            failure.append(float(count[i]/length))
            length -= count[i]
        else:
            failure.append(int(0))
    
    for i in range(N):
        answer.append((i+1,failure[i]))
    answer.sort(key = lambda x: -x[1])
    for x in answer:
        new_answer.append(x[0])
        
    return new_answer
