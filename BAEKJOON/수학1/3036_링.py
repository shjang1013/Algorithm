# 최대공약수
def gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        x, y = y, x % y
    
    return x

N = int(input())

array = list(map(int, input().split()))

for i in range(1, N):
    n = gcd(array[0], array[i])
    
    print(str(array[0]//n) + '/' + str(array[i]//n))
