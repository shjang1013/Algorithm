# 김지민과 임한수가 대결하는 라운드 번호를 출력하기
N, K, L = map(int, input().split())

count = 0

while K != L:
    if K % 2:
        K = K//2+1
    else:
        K = K//2
    
    if L % 2:
        L = L//2+1
    else:
        L = L//2
    
    count += 1

print(count)
