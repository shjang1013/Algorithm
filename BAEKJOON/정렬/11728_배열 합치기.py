# 두 배열을 합치고 정렬하여 출력하기 
import sys

N, M = map(int, input().split())

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))

A.extend(B)

print(' '.join(map(str, sorted(A))))
