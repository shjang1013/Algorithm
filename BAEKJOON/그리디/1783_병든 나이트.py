# 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수
1. 2칸 위로, 1칸 오른쪽
2. 1칸 위로, 2칸 오른쪽
3. 1칸 아래로, 2칸 오른쪽
4. 2칸 아래로, 1칸 오른쪽

# 수정한 코드
import sys

N, M = map(int, sys.stdin.readline().split())
if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M + 1) // 2))
else:
    if M < 7:
        print(min(4, M))
    else:
        print(M - 2)


1. 병든 나이트는 항상 오른쪽으로 이동한다.
2. 병든 나이트의 이동 횟수가 4번보다 크다면, 이동방법을 모두 한 번씩 사용해야 한다 => N은 3이상, M은 7이상
