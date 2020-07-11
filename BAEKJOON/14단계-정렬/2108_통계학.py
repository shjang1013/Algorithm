import collections

N = int(input())
List = sorted([int(input()) for _ in range(N)])

# 산술평균
print(round(sum(List)/N))

# 중앙값
if N % 2:
    print(List[N//2])
else:
    print(round((List[N//2-1]+List[N//2])/2, 1))

# 최빈값
l = collections.Counter(List).most_common()
if len(l) == 1 or l[0][0] != l[1][0]:
    print(collections.Counter(List).most_common()[0][0])
else:
    print(collections.Counter(List).most_common()[1][0])

# 범위
print(List[N-1]-List[0])
