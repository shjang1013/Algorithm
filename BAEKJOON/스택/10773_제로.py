# 0을 외치면, 가장 최근에 쓴 수 pop()
import sys

N = int(input())

stack = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))
