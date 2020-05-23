# 나의 코드
def solution(n):
    answer = [0]
    for i in range(n-1):
        temp = answer.copy()
        temp.reverse()
        for j in range(len(temp)):
            if temp[j] & 1:
                temp[j] = 0
            else:
                temp[j] = 1
        answer = answer + [0] + temp
    
    return answer

# 다른 코드
def solution(n):
    answer = [0]
    for i in range(1,n):
        temp = [1-j for j in answer]
        answer = answer + [0] + temp[::-1]
    
    return answer

# 종이접기 규칙
1. 맨 처음 접은 한 가운데 0을 중심으로 대칭되는 위치에 있는 숫자는 한쪽이 1이면 반대쪽은 0이다.
2. 가운데 0을 중심으로 왼쪽은 이전 answer에 저장되어 있는 리스트, 오른쪽은 순서를 뒤집어 리스트의 원소가 0이면 1로, 1이면 0으로 바꿔준 리스트
