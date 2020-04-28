# 나의 코드
def solution(s):
    return int(s)

# 다른 사람의 코드
def solution(s):
    result = 0
    
    # enumerate를 for문과 함께 사용하면 자료형의 순서와 그 값을 쉽게 알 수 있음
    # 인덱스 값이 필요할 때 enumerate 이용
    for i, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** i)

    return result
