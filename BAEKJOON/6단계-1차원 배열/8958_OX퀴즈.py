# 입력
num = int(input())
for i in range(num):
    # 테스트 케이스마다 초기화
    sum = 0
    score = 0
    test_case = input()
    for j in test_case:
        if j=='O':
            score += 1
        else:
            score = 0
        sum += score
    
    print(sum)
