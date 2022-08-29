# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return
def solution(sizes):
    MIN = []
    MAX = []

    for size in sizes:
        MIN.append(min(size))
        MAX.append(max(size))

    return max(MIN) * max(MAX)