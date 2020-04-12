# 문제
# SWEA 5203 - [파이썬 S/W 문제해결 구현 3일차] 탐욕 알고리즘 - 베이비진 게임

# 나의 코드(실패)
def BabyJin(player, p):
    if p in player:   # 받은 카드가 기존에 있을 때 triplet 찾기
        player[p] += 1
        if player[p] >= 3: # triplet
            return True

    else:  # 받은 카드가 기존에 없을 때 run 찾아보기
        player[p] = 1
        if p - 1 in player:
            if p - 2 in player or p + 1 in player:
                return True
            elif p + 1 in player and p + 2 in player:
                return True
        return False


T = int(input())

for tc in range(T):
    List = list(map(int, input().split()))
    
    result = 0
    
    player1 = player2 = []
    
    for i in range(len(List)):
        # 짝수번째 카드는 p1에게 주고 게임이 끝나면
        if i % 2 == 0:
            player1.append(List[i])
            if BabyJin(player1, List[i]):
                result = 1
            break
        # 홀수번째 카드는 p2에게 주고 게임이 끝나면
        if i % 2 == 1:
            player2.append(List[i])
            if BabyJin(player2, List[i]):
                result = 2
            break

    print('#%d %d' %(tc+1, result))
