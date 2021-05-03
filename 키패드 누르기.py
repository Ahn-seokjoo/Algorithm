def solution(numbers, hand):
    left_key = [1,4,7]
    right_key = [3,6,9]
    answer = ''
    hand_position = ['*','#']
    
    position = { 1 :(0,0), 2:(0,1), 3: (0,2),
                 4 :(1,0), 5:(1,1), 6: (1,2),
                 7 :(2,0), 8:(2,1), 9: (2,2),
                '*':(3,0), 0:(3,1), '#' :(3,2)
    }
    for num in numbers:
        if num in left_key:
            hand_position[0] = num
            answer += 'L'
        elif num in right_key:
            hand_position[1] = num
            answer +='R'
        else:
            near_hand = get_near_hand(position,hand_position[0],hand_position[1],num,hand)
            if near_hand =='L':
                hand_position[0] = num
                answer += 'L'
            else:
                hand_position[1] = num
                answer +='R'
    return answer
def get_near_hand(position,l,r,num,hand):
    left_distance = abs(position[l][0] - position[num][0]) + abs(position[l][1]-position[num][1])
    right_distnace = abs(position[r][0] - position[num][0]) + abs(position[r][1]-position[num][1])
    if left_distance == right_distnace:
        near_hand = 'L' if hand == 'left' else 'R'
    else:
        near_hand = 'L' if left_distance < right_distnace else 'R'
    return near_hand
