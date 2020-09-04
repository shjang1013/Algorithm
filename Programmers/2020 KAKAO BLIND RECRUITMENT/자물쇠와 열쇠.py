# 완전 탐색
# 2차원 리스트 90도 회전하기
def rotate_matrix(a):
    n = len(a) # 행
    m = len(a[0]) # 열
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인하기
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환하기
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 회전에 따라 자물쇠에 열쇠가 맞는지 확인하기
    for rotation in range(4):
        key = rotate_matrix(key) # 열쇠 회전하기
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사하기
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기 -> 새로운 자물쇠에 열쇠가 정확히 들어 맞지 않은 경우
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

print(solution([[0,0,0],[1,0,0],[0,1,1]], [[1,1,1], [1,1,0],[1,0,1]]))

# 주의할 점
1. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만
2. 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
# 풀이
1. 최대 4번까지 배열을 회전시키면서 가능한 경우를 모두 탐색한 다음, 자물쇠의 모든 홈을 채워 비어있는 곳이 없도록 할 수 있다면 true를, 그렇지 않다면 false를 리턴한다.
2. key와 lock을 순서대로 맞춰보는 방법 중 하나는 우선 lock배열을 가로, 세로 길이가 3배인 새로운 배열의 중앙부분으로 옮긴 후, key 배열을 순서대로 이동시키면서 겹치는 부분만 확인하면 된다. 이때 겹치는 부분은 자물쇠의 모든 홈이 채워지더라도 겹치지 않는 부분에 여전히 자물쇠의 홈 부분이 남아있을 수 있으므로 모든 홈이 채워졌는지를 정확하게 확인해야 한다.
