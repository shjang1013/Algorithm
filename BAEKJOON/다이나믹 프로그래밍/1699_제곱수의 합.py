# 주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력하기 
import math

N = int(input())

S = int(math.sqrt(N))

array = [i**2 for i in range(1, S+1)]

d = [i for i in range(N+1)]

# 다이나믹 프로그래밍
d[0] = 0

for i in range(len(array)):
    for j in range(array[i], N+1):
        d[j] = min(d[j], d[j - array[i]] + 1)

print(d[N])
