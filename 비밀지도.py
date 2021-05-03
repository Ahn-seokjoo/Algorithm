def solution(n, arr1, arr2):
    arr = list(map(lambda a : a[0] | a[1] ,zip(arr1,arr2)))
    arr = list(map(lambda a : '0'*(n-len(bin(a)[2:])) + bin(a)[2:], arr))
    answer = []
    for i in arr:
        i = i.replace('1','#')
        i = i.replace('0',' ')
        answer.append(i)
    
    return answer
