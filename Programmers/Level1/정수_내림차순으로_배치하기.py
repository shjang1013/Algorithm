# 나의 코드
def solution(n):
    # n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 *정수* 리턴
    return int(''.join(sorted(str(n), reverse=True)))

