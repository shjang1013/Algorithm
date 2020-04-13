import sys

N = int(input())
for i in range(N):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)
