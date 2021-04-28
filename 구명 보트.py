def solution(people, limit):
    people.sort()
    answer = 0
    i ,j = 0, len(people) -1
    while i<= j:
        answer += 1
        if people[j] + people[i] <= limit :
            i += 1
        j -= 1
        
    return answer
  #이런식으로 접근시에 인덱싱이 아닌, 처음부터 순서대로 뒤에서 내려올 수 있다
