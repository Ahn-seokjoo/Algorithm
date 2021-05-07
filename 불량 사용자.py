from itertools import permutations
def check(banned_ids,candidate_users):
    for i in range(len(banned_ids)):
        if len(banned_ids[i]) != len(candidate_users[i]): # 길이가 다르면 false 리턴
            return False
        if isMatchId(banned_ids[i], candidate_users[i]) is False:
            return False
    return True

def isMatchId(ban_id,user_id):
    for i in range(len(ban_id)):
        if ban_id[i] == '*': continue # *경우에는 다음 문자로 넘어감
        elif ban_id[i] != user_id[i]: # 문자가 다른 경우 false 리턴
            return False
    return True

def solution(user_ids, banned_ids):
    ans = list()
    
    for candidate_users in permutations(user_ids,len(banned_ids)):
        if check(banned_ids, candidate_users) is True:
            candidate_users = set(candidate_users)
            if candidate_users not in ans:
                ans.append(candidate_users)
    return len(ans)
            
