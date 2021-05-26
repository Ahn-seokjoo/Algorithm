def solution(array, commands):
    resultlist = []
    templist = []
    count = len(commands)
    while(1):
        for i in range(count):
            templist = array[commands[i][0]-1:commands[i][1]]
            templist.sort()
            resultlist.insert(i,templist[commands[i][2]-1])
            count -= 1
        break;
    return(resultlist)
    
    ##이렇게 풀었으나
    ## 다른사람의 답중에서 한줄짜리 코드를 보고 다시 공부해야겠음을 느낌

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
