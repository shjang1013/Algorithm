# 나의 코드
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i

    return answer

# 다른 사람의 코드
def solution(n):
    answer = 0
    # n/2의 수들만 검사하면 성능이 향상됨
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            answer += i

    return answer + n

# 참고할 것 : string.ascii_lowercase, string.ascii_uppercase 사용
