# 문제
# SWEA 5176 - [파이썬 S/W 문제해결 기본 8일차] Tree - 이진탐색

# 나의 코드
def inorder(S, E): # 처음으로 대입해야 하는 1을 count 변수를 통해 초기화한 후, 재귀탐색을 통해 왼쪽 가장 깊은 곳까지 탐색한다. 더 이상 왼쪽 아래로 내려갈 수 없을 때 count에 담아둔 1을 해당 인덱스에 대입하고 count를 1을 증가시킨다.
    global count
    if S <= E:
        inorder(S*2, E)
        Tree[S] = count
        count += 1
        inorder(S*2+1, E)

T = int(input())

for tc in range(T):
    N = int(input())
    
    Tree = [0]*(N+1)
    count = 1
    inorder(1, N)
    
    print("#%d %d %d" %(tc+1, Tree[1], Tree[N//2]))
