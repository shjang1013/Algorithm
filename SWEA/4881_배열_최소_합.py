# 문제
# SWEA 4881 - [파이썬 S/W 문제해결 기본 5일차] Stack2 - 배열 최소 합

# 나의 코드(시간 초과)
# 백트래킹 기반의 재귀 함수를 이용한 배열의 최소 합 구하기
def backtracking(row, result):
    global min # 최소 합
    
    if row == N:
        if result < min:
            min = result
        return min
    
    # 백트래킹 기반의 재귀 함수
    for i in range(N):
        if check[i] == False:
            check[i] = True
            if min > result:
                backtracking(row+1, result+array[row][i])
            check[i] = False

    return min

# 입력값
T = int(input())

for tc in range(T):
    # 최소 합을 구하기 위한 변수
    min = 10000
    
    N = int(input())
    
    # 배열
    array = []
    # 한 번 선택한 항목을 다시 선택하지 않도록 하기 위해 별도의 플래그 배열을 사용
    check = [False] * N
    
    for i in range(N):
        array.append(list(map(int, input().split())))

    print("#%d %d" %(tc+1, backtracking(0,0)))


# 수정한 코드
# 백트래킹 기반의 재귀 함수를 이용한 배열의 최소 합 구하기
def backtracking(row, result):
    global min  # 최소 합
    
    if row == N:
        if result < min:
            min = result
        return min
    
    # 백트래킹 기반의 재귀 함수
    for i in range(N):
        if check[i] == False:
            check[i] = True
            # 최소의 합이 더 클 경우에만 backtracking 실행
            if min > result:
                backtracking(row + 1, result + array[row][i])
            check[i] = False

    return min

# 입력값
T = int(input())

for tc in range(T):
    # 최소 합을 구하기 위한 변수
    min = 10000
    
    N = int(input())
    
    # 배열
    array = []
    # 한 번 선택한 항목을 다시 선택하지 않도록 하기 위해 별도의 플래그 배열을 사용
    check = [False] * N
    
    for i in range(N):
        array.append(list(map(int, input().split())))

    print("#%d %d" % (tc + 1, backtracking(0, 0)))
