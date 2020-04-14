N = int(input())

rank = [1] * N

Big = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        # 키와 몸무게가 더 크고 많이 나갈경우
        if Big[i][0] > Big[j][0] and Big[i][1] > Big[j][1]:
            rank[j] += 1
        elif  Big[i][0] < Big[j][0] and Big[i][1] < Big[j][1]:
            rank[i] += 1

# 등수 출력
for i in range(N):
    print(rank[i], end=" ")
