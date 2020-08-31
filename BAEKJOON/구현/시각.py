# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력하기
N = int(input())

count = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            # 3이 하나라도 포함되는 경우 
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)
