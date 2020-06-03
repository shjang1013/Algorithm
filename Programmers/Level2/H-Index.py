# 나의 코드(실패) - 예외 : [2,2,2,2,2]
def solution(citations):
    citations.sort(reverse = True)
    
    for i in range(len(citations), 0, -1):
        answer = 0
        
        for j in citations:
            if i <= j:
                answer += 1
    
        if  i == answer:
            return answer

    return 0

# 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용되었다면 h의 최댓값 리턴

# 수정한 코드
def solution(citations):
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        if n <= i:
            return i

    # citations의 길이보다 각각의 인용 횟수가 크거나 같은 경우
    return len(citations)
