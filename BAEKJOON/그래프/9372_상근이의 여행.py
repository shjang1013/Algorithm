# 모든 국가가 연결되어 있으므로 비행기 종류의 최소 개수 : 국가 수-1 
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    for _ in range(M):
        a, b = map(int, input().split())
    
    print(N-1)
