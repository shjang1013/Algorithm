# 꿍 피보나치 값 출력하기
d = [0] * 68

# 피보나치 함수
d[0] = 1
d[1] = 1

d[2] = 2

d[3] = 4

for i in range(4, 68):
    d[i] = d[i-1] + d[i-2] + d[i-3] + d[i-4]

N = int(input())

for _ in range(N):
    t = int(input())
    
    print(d[t])
