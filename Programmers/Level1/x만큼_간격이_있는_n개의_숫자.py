# 나의 코드
def solution(x, n):
    # 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴
    if x == 0:
        answer = [0]*n
    elif x > 0:
        answer = [i for i in range(x, x * n + 1, x)]
    else:
        answer = [-i for i in range(-x, -x * n + 1, -x)]
    
    return answer


# 다른 코드
def solution(x, n):
    return [i * x + x for i in range(n)]

