# 시간 초과 - 재귀로 코드를 작성했으나 실패
# k층의 n호에 살기 위해서는 (k-1)층의 1호부터 n호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
def floor(k, n):
    num = 0
    if k == 0:
        return n
    for i in range(1,n+1):
        num += floor(k-1, i)
    
    return num

T = int(input())

for _ in range(T):
    print(floor(int(input()), int(input())))

# 수정한 코드
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    num = [i for i in range(1,n+1)]

    for _ in range(k):
        for i in range(1,n):
            num[i] += num[i-1]

    print(num[n-1])
