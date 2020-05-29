# 나의 코드
from itertools import permutations

def CheckScore(baseball, P, S, B):
    strike = 0
    for i in range(3):
        if baseball[i] == P[i]:
            strike += 1

    # 주어진 스트라이크 수와 다를 경우
    if S != strike:
        return False
    
    # 주어진 스트라이크 수와 같을 경우
    ball = len(set(baseball) & set(P)) - strike
    
    # 주어진 볼의 수와 같을 경우
    if B != ball:
        return False
    # 다를 경우
    return True


def solution(baseball):
    List = list(permutations([i for i in range(1, 10)], 3))
    
    for i in baseball:
        for j in List[:]:
            # baseball 세자리 수, 순열, 스트라이크, 볼
            if not CheckScore(list(map(int, list(str(i[0])))), j, i[1], i[2]):
                List.remove(j)

    return len(List)
