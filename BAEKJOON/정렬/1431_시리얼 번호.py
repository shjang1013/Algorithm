N = int(input())

array = []

for _ in range(N):
    n = input()
    sum = 0
    for i in n:
        if i.isdigit():
            sum += int(i)
    array.append((n, sum))

1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다.
3. 1, 2번 조건으로도 비교할 수 없으면, 사전순으로 비교한다.
array = sorted(array, key=lambda x:(len(x[0]), x[1], x))

# 출력
for j in array:
    print(j[0])
