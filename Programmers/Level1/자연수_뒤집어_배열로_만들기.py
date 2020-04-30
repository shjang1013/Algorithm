# 나의 코드
def solution(n):
    # 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴 
    return list(map(int, reversed(str(n))))
