# 나의 코드
def solution(priorities, location):
    answer = 0
    MAX = max(priorities)
    
    while priorities:
        temp = priorities.pop(0)
        if MAX == temp:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            MAX = max(priorities)
    
        else:
            priorities.append(temp)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1

    return answer
