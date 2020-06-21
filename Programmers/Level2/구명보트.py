# 나의 코드
def solution(people, limit):
    people.sort()
    answer = 0
    i = 0
    j = len(people)-1
    
    while i<=j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    
    return answer

# index 이용하여 구현할 것!
# 최대 2명, 가장 가벼운 사람 + 가장 무거운 사람 
