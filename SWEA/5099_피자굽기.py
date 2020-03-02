# 문제
# SWEA 5099 - [파이썬 S/W 문제해결 기본 6일차] Queue - 피자 굽기

# 나의 코드
T = int(input())

for tc in range(T):
    # 화덕의 크기, 피자 개수
    N, M = map(int, input().split())
    
    # 치즈의 양
    C = list(map(int, input().split()))
    
    queue = [[i+1, C[i]] for i in range(len(C))]
    
    # 화덕
    oven = [queue.pop(0) for _ in range(N)]
    
    while len(oven) != 1:
        temp = oven.pop(0)
        num = temp[1]//2
        if num != 0:
            oven.append([temp[0], num])
        else:
            if queue:
                oven.append(queue.pop(0))

    print("#%d %d" %(tc+1, oven[0][0]))

