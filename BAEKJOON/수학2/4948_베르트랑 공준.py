# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
while True:
    N = int(input())
    
    if N == 0:
        break
    
    count = 0
    sosu = [False, False] + [True]*(2*N-1)
    
    for i in range(2, 2*N+1):
        if sosu[i]:
            for j in range(2*i, 2*N+1, i):
                sosu[j] = False

    print(sum(sosu[N+1:2*N+1]))
