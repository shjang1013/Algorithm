# N의 가장 작은 생성자 구하기

T = int(input())

result = 0

for i in range(1, T+1):
    result = i + sum(list(map(int, str(i))))
    
    # 생성자
    if result == T:
        print(i)
        break
    
    # 생성자가 존재하지 않는 경우
    elif i == T:
        print(0)

