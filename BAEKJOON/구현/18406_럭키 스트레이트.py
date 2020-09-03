# 왼쪽 부분의 각 자릿수의 합 = 오른쪽 부븐의 각 자릿수의 합
N = list(map(int, list(input())))

if sum(N[:len(N)//2]) == sum(N[len(N)//2:]):
    print("LUCKY")
else:
    print("READY")
