# 소인수분해 결과를 한 줄에 오름차순으로 출력하기
# 소인수분해 : 합성수를 소수의 곱으로 나타내는 방법을 말한다.
# 따라서, 먼저 에라토스테네스의 체를 통해 소수를 구한다.

# 나의 코드
import sys

N = int(sys.stdin.readline())

a = [False, False] + [True]*(N-1)

primes = []

for i in range(2, N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

i = 0

List = []

while N > 1:
    if N % primes[i] == 0:
        List.append(primes[i])
        N //= primes[i]
    else:
        i += 1

print('\n'.join(map(str, List)))


# 다른 코드
N = int(input())

i = 2

while N > 1 :
    # 소수인 2부터 나눗셈 반복 => 합성수로는 나눠지지 않음
    if N % i == 0:
        N //= i
        print(i)
    else :
        i += 1
