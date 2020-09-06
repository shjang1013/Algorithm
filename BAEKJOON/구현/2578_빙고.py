# 사회자가 몇 번째 수를 부른 후 철수가 빙고(3줄 이상)를 외치게 되는지 출력하기
def checkBingo(a):
    sum = 0
    # 가로 빙고
    for i in range(5):
        if a[i].count(1) == 5:
            sum += 1

    # 세로 빙고
    n = 0
    for i in range(5):
        for j in range(5):
            if a[j][i] == 1:
                n += 1
        if n == 5:
            sum += 1
        else:
            n = 0

    # 대각선 빙고(왼쪽)
    n = 0
    for i in range(5):
        if a[i][i] == 1:
            n += 1
    if n == 5:
        sum += 1
    
    # 대각선 빙고(오른쪽)
    n = 0
    for i in range(5):
        if a[i][4-i] == 1:
            n += 1
    if n == 5:
        sum += 1
    
    # 3줄 이상 빙고 
    if sum >= 3:
        return True
    
    return False


cheolsoo = [list(map(int, input().split())) for _ in range(5)]

moderator = []

for i in range(5):
    moderator.extend(list(map(int, input().split())))


checkList = [[0]*5 for _ in range(5)]

for i in range(len(moderator)):
    for l in range(5):
        for k in range(5):
            if cheolsoo[l][k] == moderator[i]:
                checkList[l][k] = 1
                break

    if i >= 10:
        if checkBingo(checkList):
            print(i+1)
            break
