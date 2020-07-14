num = int(input())

for i in range(num):
    # 반복횟수, 테스트케이스
    R, test_case = input().split()
    for j in test_case:
        print(int(R)*j, end='')
    print()
