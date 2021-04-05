import heapq
def solution(food_times, k):
    #전체 음식 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        # 음식 시간 음식 번호 형태로 우선순위 큐에 삽입
        heapq.heappush(q,(food_times[i],i +1))
        
    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다먹은 음식 시간
    length = len(food_times) #남은 음식의 개수
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now- previous) * length
        length -= 1 #다먹은 음식 제외
        previous = now #이전 음식 시간 재설정
        
    result = sorted(q,key=lambda x: x[1]) #음식 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
    
    #너무 어려움... 다시 풀어볼 수있도록 함
