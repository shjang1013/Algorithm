# 정렬된 두 묶음의 숫자 카드가 있을 때 각 묶음의 카드의 수가 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데 A+B번의 비교를 해야함
# 최소한 몇 번의 비교가 필요한지를 구하는 프로그램 작성
import heapq
import sys

N = int(input())
cards = []

for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

result = 0

while len(cards) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)
    
    result += (one + two)
    
    # 카드 묶음 다시 넣기
    heapq.heappush(cards, one + two)

print(result)

