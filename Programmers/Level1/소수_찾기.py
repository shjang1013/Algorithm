# 나의 코드(시간 초과)
def solution(n):
    List = []
    for i in range(2, n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
    
        # 소수 : 1과 자기 자신으로밖에 나누어떨어지지 않는 1 이외의 정수
        if count == 2:
            List.append(j)

return len(List)

'''
    에라토스테네스의 체
    
    1. 1은 제거
    2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.
    3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다.
    4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다.
    5. 이처럼 a[i] == True일 때, 이를 반복한다.

'''

# 에라토스테네스의 체
def solution(n):
    a = [False, False] + [True] * (n - 1)
    answer = []
    
    for i in range(2, n + 1):
        if a[i]:
            answer.append(i)
            # 배수 False
            for j in range(2 * i, n + 1, i):
                a[j] = False

    return len(answer)


# set을 이용한 에라토스테네스의 체
def solution(n):
    answer = set(range(2, n+1))
    
    for i in range(2,n+1):
        if i in answer:
            # 배수 지우기
            answer -= set(range(2*i, n+1, i))
    return len(num)
