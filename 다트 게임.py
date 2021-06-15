import re
#eval 쓰면 문자열을 계산한다

def solution(dartResult):
    charConv ={'S':'**1','D':'**2','T':'**3','#':'*-1'}
    result =[]
    #숫자랑 문자를 나눔
    dartResult = re.sub('([SDT][*#]?)','\g<1> ',dartResult).split()
    print(dartResult)
    for dart in dartResult:
        for word in dart:
            dart = dart.replace(word,charConv.get(word,word))
        if dart[-1] == '*':
            dart += '2'
            if result :
                result[-1] = result[-1][:-1] +'*2+'
        dart += '+'
        result.append(dart)
        
    return eval(''.join(result)[:-1])

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    
    dart = p.findall(dartResult)            
    for i in range(len(dart)):                # 정규표현식으로 갈무리된 문자열들
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    answer = sum(dart)
    return answer
