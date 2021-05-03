import re
from itertools import permutations

def solution(expression):
    expression = re.split('([-+*])',expression)
    results = []
    operators = list(permutations(['-','+','*'],3))
    
    for opertator in operators:
        exp = expression[:] #리스트 전체 복사
        for op in opertator:
            while op in exp:
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1]))
                del exp[idx:idx+2]
        results.append(abs(int(exp[0]))) # 0번을 하면 숫자만 나옴
        
    return max(results)
