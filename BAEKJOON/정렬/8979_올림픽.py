# 각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 출력
import sys

N, K = map(int, input().split())

Country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

Country = sorted(Country, key=lambda x:(x[1], x[2], x[3]), reverse=True)

gold = silver = Bronze = 0

rank = 1

print(Country)

for i in range(N):
    if gold != Country[i][1] or silver != Country[i][2] or bronze != Country[i][3]:
        rank = i+1
        gold = Country[i][1]
        silver = Country[i][2]
        bronze = Country[i][3]
    
    if K == Country[i][0]:
        break

print(rank)
