# 문제
# SWEA 5178 - [파이썬 S/W 문제해결 기본 8일차] Tree - 노드의 합

# 나의 코드
T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    
    # 완전 이진 트리
    Tree = [0] * (N+1)
    
    for _ in range(M):
        n, d = map(int, input().split())
        Tree[n] = d
    
    # N이 짝수일 경우 노드가 하나만 남는다.
    if N % 2 == 0:
        Tree[N // 2] = Tree[N]
        N -= 1
    
    for i in range(N, 1, -2):
        Tree[i//2] = Tree[i] + Tree[i-1]
    
    print("#%d %d" %(tc+1, Tree[L]))
