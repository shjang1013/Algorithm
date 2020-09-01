# 캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 이뤄진 N X M 크기의 정사각형으로, 각각의 칸은 육지 또는 바다이다.
# 캐릭터는 동서남북 중 한 곳을 바라본다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳으르 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 횐전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

# 수정한 코드

# N, M 입력 받기
N, M = map(int, input().split())

# 방문한 위치를 저장하기
visited = [[0] * M for _ in range(N)]

# 현재 캐릭터의 X좌표, Y좌표, 방향 입력 받기
x, y, d = map(int, input().split())

# 현재 좌표 방문 처리
visited[x][y] = 1

# 전체 맵 정보를 입력 받기
Map = []

for _ in range(N):
    Map.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]

dy = [0, 1, 0, -1]


# 시뮬레이션 시작
count = 1

# 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우를 위한 변수
turn = 0

while True:
    # 왼쪽으로 회전
    d -= 1
    
    if d == -1:
        d = 3

    nx = x + dx[d]
    ny = y + dy[d]

    # 가보지 않은 경우 & 육지인 경우
    if visited[nx][ny] == 0 and Map[nx][ny] == 0:
        # 방문 처리
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn = 0
        continue
    # 가보지 않은 칸이 없는 경우 & 바다인 경우
    else:
        turn += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 이동하기
        if Map[nx][ny] == 0:
            x, y = nx, ny
            turn = 0
        else:
            break

print(count)

# (1,1) (1,2) (2,2) 3개
