# 연산을 하는 횟수의 최솟값 출력하기
정수가 X에 사용할 수 있는 연산
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

# 나의 코드
N = int(input())

d = [0] * 1000001

for i in range(2, N+1):
    d[i] = d[i-1] + 1
    
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)


print(d[N])
