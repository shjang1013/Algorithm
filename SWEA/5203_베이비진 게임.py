# 문제
# SWEA 5203 - [파이썬 S/W 문제해결 구현 3일차] 탐욕 알고리즘 - 베이비진 게임

# 나의 코드(성공)
def babyGin(player, card, i):
    if player[i] >= 3:
        return True
    
    else:
        if i - 1 in card:
            if i - 2 in card or i + 1 in card:
                return True
        elif i + 1 in card and i + 2 in card:
            return True

    return False

T = int(input())

for tc in range(T):
    cards = list(map(int, input().split()))
    
    card1 = []
    card2 = []
    
    # count
    player1 = [0] * 10
    player2 = [0] * 10
    
    result = 0
    
    for i in range(len(cards)):
        if i % 2 == 0:
            card1.append(cards[i])
            player1[cards[i]] += 1
            if babyGin(player1, card1, cards[i]):
                result = 1
                break
    
        else:
            card2.append(cards[i])
            player2[cards[i]] += 1
            if babyGin(player2, card2, cards[i]):
                result = 2
                break

    print("#%d %d" %(tc+1, result))

