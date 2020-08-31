# 두 사람이 볼링공을 고르는 경우의 수를 출력하기
import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

ball = list(map(int, sys.stdin.readline().split()))

count = 0

# 두 사람은 서로 무게가 다른 볼링공을 고르려고 함 
for i in itertools.combinations(ball, 2):
    if i[0] != i[1]:
        count += 1

print(count)


# 다른 코드
import sys

N, M = map(int, sys.stdin.readline().split())

ball = list(map(int, sys.stdin.readline().split()))

# 1-10까지의 무게를 담을 수 있는 리스트
List = [0] * 11

for i in ball:
    List[i] += 1

count = 0

for i in range(1, M+1):
    N -= List[i]            # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    count += List[i] * N    # B가 선택하는 경우의 수와 곱하기

print(count)
