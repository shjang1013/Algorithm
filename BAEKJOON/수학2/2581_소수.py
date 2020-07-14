# M이상 N이하의 자연수 중 소수인 것을 모두 골라 소수의 합 / 최솟값 찾기
M = int(input())
N = int(input())

sosu = [False, False] + [True]*(N-1)
List = []

for i in range(2, N+1):
    if sosu[i]:
        if M <= i <= N:
            List.append(i)
        for j in range(2*i, N+1, i):
            sosu[j] = False

if len(List) != 0: # 문제 꼼꼼하게 읽기
    print(sum(List))
    print(min(List))
else:
    print(-1)
