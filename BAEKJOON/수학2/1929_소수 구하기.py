# M이상 N이하의 소수 모두 출력하기
M, N = map(int, input().split())

sosu = [False, False] + [True]*(N-1)
List = []

for i in range(2, N+1):
    if sosu[i]:
        if M <= i <= N:
            List.append(i)
        for j in range(2*i, N+1, i):
            sosu[j] = False

for i in List:
    print(i)
