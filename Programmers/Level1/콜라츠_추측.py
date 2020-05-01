# 나의 코드
def solution(num):
    answer = 0
    # 주어진 수가 1이 될 때까지 작업을 반복
    while num != 1:
        # 훌수라면 3을 곱하고 1을 더하기
        if num & 1:
            num = num * 3 + 1
        # 짝수라면 2로 나누기
        else:
            num //= 2
        answer += 1
        
        # 작업이 500번을 반복해도 1이 되지 않는다면 -1 반환하기
        if answer >= 500:
            answer = -1
            break

    return answer
