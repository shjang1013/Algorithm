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
