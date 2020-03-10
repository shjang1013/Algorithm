# 문제
# SWEA 5177 - [파이썬 S/W 문제해결 기본 8일차] Tree - 이진 힙

# 나의 코드
def heap(i):
    while i != 1:
        if Tree[i] < Tree[i // 2]:
            Tree[i], Tree[i // 2] = Tree[i // 2], Tree[i]
        i //= 2


T = int(input())

for tc in range(T):
    N = int(input())
    List = list(map(int, input().split()))
    
    # 초기화
    Tree = [0]*(N+1)
    
    # 숫자를 차례로 입력할 떼마다 힙 정렬
    for i in range(1,N+1):
        Tree[i] = List[i-1]
        heap(i)
    
    result = 0
    
    # 마지막 노드의 조상 노드에 저장된 정수의 합
    while N != 1:
        N //= 2
        result += Tree[N]
    
    
    print("#%d %d" %(tc+1, result))
