# 나의 코드
def solution(d, budget):
    # 최대 몇 개의 부서에 물품을 지원할 수 있는지 리턴하기 
    sum = answer =  0
    
    for i in sorted(d):
        if sum + i <= budget:
            sum += i
            answer += 1

    return answer



# 다른 코드
def solution(d, budget):
    d.sort()
    
    while budget < sum(d):
        d.pop()
    
    return len(d)

