# 문제
# SWEA 5202 - [파이썬 S/W 문제해결 구현 3일차] 탐욕 알고리즘 - 화물 도크

# 나의 코드
T = int(input())
for tc in range(T):
    N = int(input())
    
    time = []
    Lorry = []
    
    for i in range(N):
        time.append(list(map(int, input().split())))

    time.sort(key = lambda i:i[1])

    Lorry.append(time[0])
 
    for k in range(N):
        if Lorry[-1][1] <= time[k][0]:
            Lorry.append(time[k])
            i += 1

    print("#%d %d" %(tc+1, len(Lorry)))
