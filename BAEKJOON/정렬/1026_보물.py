# S의 최솟값 출력하기 
import sys

N = int(sys.stdin.readline())

# A는 재배열 가능
A = sorted(list(map(int, sys.stdin.readline().split())))

# B는 재배열 불가능
B = list(map(int, sys.stdin.readline().split()))

# 최솟값 출력하기
S = 0

for i in range(N):
    S += (A[i] * B.pop(B.index(max(B))))

print(S)
