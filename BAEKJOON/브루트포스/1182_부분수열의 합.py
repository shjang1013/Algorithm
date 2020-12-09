# 부분수열의 합이 S가 되는 경우의 수 구하기
import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())

array = list(map(int, input().split()))

count = 0

for i in range(1, N+1):
    # 부분수열 구하기 
    c = combinations(array, i)
    
    for j in c:
        if sum(j) == S:
            count += 1

print(count)
