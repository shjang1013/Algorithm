# 문제
# SWEA 5201 - [파이썬 S/W 문제해결 구현 3일차] 탐욕 알고리즘 - 컨테이너 운반

# 나의 코드

# 트럭당 한 개의 컨테이너를 운반할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

T = int(input())
for tc in range(T):
    # 컨테이너 수, 트럭 수
    N, M = map(int, input().split())
    
    # 화물의 무게
    w = list(map(int, input().split()))
    w.sort(reverse = True)
    # 트럭의 무게
    t = list(map(int, input().split()))
    t.sort(reverse = True)
    
    sum = i = j = 0
    
    while i < len(w) and j < len(t):
        if w[i] <= t[j]:
            sum += w[i]
            i += 1
            j += 1
        # 트럭의 적재용량을 초과하는 경우
        else:
            i += 1

    print("#%d %d" %(tc+1, sum))


# 다른 풀이

T = int(input())
for tc in range(T):
    # 컨테이너 수, 트럭 수
    N, M = map(int, input().split())
    # 화물의 무게
    Mat_Weight = list(map(int, input().split()))
    # 트럭의 무게
    Truck_Weight = list(map(int, input().split()))
    
    result = 0
    for i in range(M):
        temp = 0
        for unit_weight in Mat_Weight:
            if Truck_Weight[i] >= unit_weight and unit_weight >= temp:
                temp = unit_weight
        if temp != 0:
            Mat_Weight.remove(temp)
        result += temp
    
    print('#%d %d' %(tc+1, result))
