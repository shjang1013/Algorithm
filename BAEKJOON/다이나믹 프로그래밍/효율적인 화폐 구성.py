# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수

# 정수 N, M을 입력받기
N, M = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(N):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (M+1)

# 다이나믹 프로그래밍 진행
d[0] = 0
for i in range(N):
    for j in range(array[i], M+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

# 결과 출력
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
