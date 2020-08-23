# 집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성 
import sys

N = int(input())

place = list(map(int, sys.stdin.readline().split()))

place.sort()

# 중앙값 출력
print(place[(N-1)//2])

