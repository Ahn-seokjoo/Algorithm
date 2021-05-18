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
