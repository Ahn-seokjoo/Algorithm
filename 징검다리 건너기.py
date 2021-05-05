def solution(stones, k):
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        tmp = stones[:]
        
        for i in range(len(tmp)):
            tmp[i] -= mid
        
        cnt = 0
        check = False
        
        for i in range(len(tmp)):
            if tmp[i] <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                check = True
                break
        if check == True:
            right = mid - 1
        else:
            left = mid + 1
    return left
