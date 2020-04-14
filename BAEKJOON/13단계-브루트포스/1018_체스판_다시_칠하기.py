N, M = map(int, input().split())

Chess = [input() for _ in range(N)]

black = white = 0

paint = []

# 8*8 크기의 체스판으로 자르기
for i in range(N - 7):
    for j in range(M - 7):
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                # 두 수가 짝수와 짝수, 홀수와 홀수
                if (k & 1 and l & 1) or (~k & 1 and ~l & 1):
                    if Chess[k][l] != 'W':
                        white += 1
                # 두 수가 짝수와 홀수, 홀수와 짝수
                else:
                    if Chess[k][l] != 'B':
                        white += 1
    
        if white >= 64 - white:
            paint.append(64 - white)
        else:
            paint.append(white)
        
        # 초기화
        white = 0

print(min(paint))
