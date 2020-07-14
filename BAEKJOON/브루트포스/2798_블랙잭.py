import itertools

# N장의 카드, M을 넘지 않으면서 M에 최대한 가까운 카드
N, M = map(int, input().split())

card = list(map(int, input().split()))

# N장의 카드 중에서 3장의 카드를 골라야 한다.
perList = list(itertools.permutations(card, 3))

result = [sum(perList[i]) for i in range(len(perList)) if sum(perList[i]) <= M]

print(max(result))

