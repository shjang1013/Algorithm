while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break

# 몇 개의 테스트 케이스가 주어지는지 모름. 따라서 EOF까지 받아야 함

# 여러 줄을 입력받고 싶을 때는 sys.stdin 이용

'''
import sys

for line in sys.stdin:
    A,B = map(int, line.split())
    print(A+B)
'''
