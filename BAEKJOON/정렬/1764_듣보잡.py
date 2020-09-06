# 듣도 못한 사람의 명단과 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

N_List = [input() for _ in range(N)]

M_List = [input() for _ in range(M)]

# 사전순으로 정렬하기
sorted_list = sorted(list(set(N_List) & set(M_List)))

print(len(sorted_list))

for i in sorted_list:
    print(i[:-1])
