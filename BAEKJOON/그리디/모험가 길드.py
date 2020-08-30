# 여행을 떠날 수 있는 그룹 수의 최댓값 출력하기
N = int(input())

adventure = sorted(list(map(int, input().split())))

group = 0 # 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in adventure:     # 공포도를 낮은 것부터 하나씩 확인하기
    count += 1           # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:       # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성하기
        group += 1       # 총 그룹의 수 증가시키기
        count = 0        # 현재 그룹에 포함된 모험가의 수 초기화하기 

print(group)
