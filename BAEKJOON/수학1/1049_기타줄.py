# 적어도 기타줄 N개를 사기 위해 필요한 돈의 수를 구하기
# 한 브랜드만 이용하지 않아도 된다.

N, M = map(int, input().split())

# 6줄 패키지
six = 100001
# 낱개 가격
one = 100001

# 브랜드별로 패키지, 낱개 가격 입력받기
for _ in range(M):
    brand = list(map(int, input().split()))

    # 브랜드에서 패키지, 낱개 기타줄이 가장 저렴한 제품 찾기
    six = min(six, brand[0])
    one = min(one, brand[1])


# 끊어진 기타줄이 6개 이상일 경우
if N > 6:
    # 패키지로만, 패키지 + 낱개, 낱개만
    print(min((N//6+1)*six, N//6*six + (N%6)*one, N*one))
else:
    print(min(six, N*one))
