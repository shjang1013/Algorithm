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
    
    # 카드 묶음 다시 넣기
    result += (one + two)
    heapq.heappush(cards, result)

print(result)

