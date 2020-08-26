# A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하라 
import sys

N, K = map(int, input().split())

A = sorted(list(map(int, sys.stdin.readline().split())))

print(A[K-1])
