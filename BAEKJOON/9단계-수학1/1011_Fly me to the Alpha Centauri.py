# x지점부터 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    
    N = 1
    count = 1
    num = y-x
    
    while num >= N:
        N += 2*count
        count += 1
    
    print(2*(count-1)-1) if num < N-(count-1) else print(2*(count-1))

# 규칙
1 1                 => 1개
2 2                 => 1개
3 3, 4 3            => 2개
5 4, 6 4            => 2개
7 5, 8 5, 9 5       => 3개
10 6, 11 6, 12 6   => 3개
.....

