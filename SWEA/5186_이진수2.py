# 문제
# SWEA 5186 - [파이썬 S/W 문제해결 구현 1일차] 시작하기 - 이진수2

# 나의 코드
T = int(input())

for tc in range(T):
    num = float(input())
    result = ''
    count = 0
    
    # 십진수 => 이진수
    while count <= 13:
        num = num * 2
        result += str(num)[0]
        num = num - int(num)
        count += 1
        if num == 0.0:
            break

    if count > 13:
        print("#%d overflow" %(tc+1))
    else:
        print("#%d %s" %(tc+1, result))
