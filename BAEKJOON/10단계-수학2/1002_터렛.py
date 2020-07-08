# 직사각형 경계선까지 가는 거리의 최솟값을 출력
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    count = 0
    if r1 > r2:
        r1, r2 = r2, r1
    
    # 거리
    d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    
    # 원이 두 점에서 만나는 경우
    if r2-r1 < d < r1+r2:
        count = 2
    
    # 두 원이 외접하는 경우(한 점), 두 원이 내접하는 경우(한 점에서 만난다)
    elif r1+r2 == d or (r2-r1 == d and d != 0):
        count = 1
    
    # 하나의 원이 다른 원을 포함하는 경우(만나지 않는다)
    elif r2-r1 > d:
        count = 0
    
    # 두 원이 멀리 떨어져 만나지 않는 경우
    elif r2+r1 < d:
        count = 0
    
    # 두 원이 일치하는 경우(무수히 많은 점에서 만난다)
    elif r2==r1 and d == 0:
        count = -1

    print(count)
