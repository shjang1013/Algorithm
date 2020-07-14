# N개의 수가 주어졌을 때, 오름차순으로 정렬하기
N = int(input())

# 입력받기
List = [int(input()) for _ in range(N)]

# 리스트 정렬하기
List.sort()

# 리스트 출력하기
for i in List:
    print(i)


# 숏코딩
for i in sorted([int(input()) for _ in range(int(input()))]):
    print(i)
