# 최대공약수
def gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        x, y = y, x % y
    
    return x

# 최소공배수
def lcm(x, y):
    return x * y // gcd(x, y)

N, M = map(int, input().split())

print(lcm(N, M))
