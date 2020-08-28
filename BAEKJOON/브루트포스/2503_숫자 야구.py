import itertools

def check(game, List, S, B):
    strike = 0
    
    for i in range(3):
        if game[i] == List[i]:
            strike += 1

    if S != strike:
        return False
    
    ball = len(set(game) & set(List)) - strike
    
    if ball != B:
        return False
    
    return True

# 메인
N = int(input())

game = [input().split() for _ in range(N)]

List = list(itertools.permutations([i for i in range(1,10)], 3))

for i in game:
    for j in List[:]:
        if not check(i[0], ''.join(map(str, j)), int(i[1]), int(i[2])):
            List.remove(j)

print(len(List))
