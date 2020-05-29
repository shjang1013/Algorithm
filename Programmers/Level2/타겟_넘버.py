# 나의 코드
answer = 0

def DFS(i, numbers, target, result):
    global answer
    
    # 마지막 값에 도달하면 종료
    if i == len(numbers):
        # 타겟과 같을 경우 answer 1을 증가
        if target == result:
            answer += 1
        return

    # 플러스일 경우
    DFS(i+1, numbers, target, result + numbers[i])
    # 마이너스일 경우
    DFS(i+1, numbers, target, result - numbers[i])


def solution(numbers, target):
    global answer
    
    # 시작
    DFS(0, numbers, target, 0)
    
    return answer
