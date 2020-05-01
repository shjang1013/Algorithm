# 나의 코드
def solution(n, m):
    answer = []
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer = [i, n*m/i]
            break

    return answer

# 다른 코드
def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d # 최댓값, 최솟값
        c, d = d, t # 최댓값 = 최솟값, 최솟값 = 최댓값과 최솟값의 나머지
    answer = [c, int(a*b/c)]

    return answer
