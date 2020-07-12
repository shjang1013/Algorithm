# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬하기 
N = int(input())

List = [tuple(map(int, input().split())) for _ in range(N)]

List = sorted(List, key = lambda x : (x[0], x[1]))

for i in List:
    print("%d %d" %(i[0], i[1]))
