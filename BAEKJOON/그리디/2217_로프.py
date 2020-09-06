# 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량 구해 출력하기
import sys

input = sys.stdin.readline

N = int(input())

List = sorted([int(input()) for _ in range(N)], reverse=True)

MAX = 0

for i in range(len(List)):
    MAX = max(MAX, List[i] * (i+1))

print(MAX)
