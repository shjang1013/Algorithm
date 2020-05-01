# 나의 코드
def solution(x):
    # 하샤드 수 : x의 자릿수의 합으로 x가 나누어떨어지는 것
    return True if x % sum(list(map(int, str(x)))) == 0 else False

# 다른 코드
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0
