# 새로운 수의 자릿수를 출력하기
N = input()

n = len(N)

count = 0

for i in range(n-1):
    count += 9*(10**i)*(i+1)

count += (int(N)-10**(n-1)+1)*n

print(count)
