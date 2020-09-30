# 각 사람이 돈을 인출하는 데 필요한 시간의 합의 최솟값 출력하기 
N = int(input())

ATM = list(map(int, input().split()))

ATM.sort()

sum = 0

for i in range(N):
    sum += ATM[i] * (len(ATM)-i)

print(sum)
