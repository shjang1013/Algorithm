# 계단 오르는 데 필요한 규칙
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계산으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

# 나의 코드
N = int(input())

stairs = [0] * 301
dp = [0] * 301

for i in range(N):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + stairs[i] + stairs[i-1], dp[i-2] + stairs[i])

print(dp[N-1])


