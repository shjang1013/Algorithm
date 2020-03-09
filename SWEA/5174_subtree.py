# 문제
# SWEA 5174 - [파이썬 S/W 문제해결 기본 8일차] Tree - subtree

# 나의 코드
def preorder(T):
    global result
    if T:
        preorder(Tree[T][0])
        preorder(Tree[T][1])
        result += 1


T = int(input())
for tc in range(T):
    
    # 간선의 개수 E, 루트 N
    E, N = list(map(int, input().split()))
    
    # 부모와 자식 노드 쌍 (노드 번호는 E+1까지 존재)
    Tree = [[0 for _ in range(2)] for _ in range(E+2)]
    l = list(map(int, input().split()))
    for i in range(0, len(l), 2):
        if Tree[l[i]][0]:
            Tree[l[i]][1] = l[i+1]
        else:
            Tree[l[i]][0] = l[i + 1]

    # N부터 전위순회하면서 존재하는 자식 노드 카운트
    result = 0
    preorder(N)
    
    # 결과 출력
    print("#%d %d" %(tc+1, result))

