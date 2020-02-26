# 문제
# SWEA 4880 - [파이썬 S/W 문제해결 기본 5일차] Stack2 - 토너먼트 카드게임

# 나의 코드
def win(l, r):
    if (card[l-1] == 1 and card[r-1] == 2) or (card[l-1] == 2 and card[r-1] == 3) or (card[l-1] == 3 and card[r-1] == 1):
        return r
    return l

def game(start, end):
    if start == end:
        return start
    
    # 분할
    left_game = game(start, (start + end) // 2)
    right_game = game((start + end) // 2 + 1, end)

    return win(left_game, right_game)

T = int(input())

for tc in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    
    result = game(1,N)
    print("#%d %d" % (tc + 1, result))
