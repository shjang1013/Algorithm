# 주어진 수 N개 중에서 소수가 몇 개인지 출력
T = int(input())

N = list(map(int, input().split()))

count = 0

sosu = [False, False] + [True]*(max(N)-1)

for i in range(2, max(N)+1):
    if sosu[i]:
        for j in range(2*i, max(N)+1, i):
            sosu[j] = False

for i in N:
    if sosu[i]:
        count += 1

print(count)
