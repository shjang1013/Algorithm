# 시간 초과
T = int(input())

for _ in range(T):
    n = int(input())
    
    sosu = [False, False] + [True]*(n-2)
    
    for i in range(2, n):
        if sosu[i]:
            for j in range(2*i, n, i):
                sosu[j] = False

    for i in range(n//2, 1, -1):
        if sosu[i] and sosu[n-i]:
            print('%d %d' %(i, n-i))
            break

# 수정한 코드
sosu = [False, False] + [True] * 9999

for i in range(2, 10001):
    if sosu[i]:
        for j in range(2 * i, 10001, i):
            sosu[j] = False

T = int(input())

for _ in range(T):
    n = int(input())
    
    for i in range(n // 2, 1, -1):
        if sosu[i] and sosu[n - i]:
            print('%d %d' % (i, n - i))
            break

# 각 테스트 케이스마다 소수 리스트를 생성하지 말고, n이 주어져 있으므로 미리 소수 리스트를 만든다.
# 에라토스테네스의 체
