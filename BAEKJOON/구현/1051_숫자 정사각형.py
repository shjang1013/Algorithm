# 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형 찾기
N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input())))

MIN = min(N, M)

result = 1

for l in range(MIN, 1, -1):
    for i in range(N-l+1):
        for j in range(M-l+1):
            if array[i][j] == array[i][j+l-1] == array[i+l-1][j] == array[i+l-1][j+l-1] :
                if result < l:
                    result = l

print(result**2)
