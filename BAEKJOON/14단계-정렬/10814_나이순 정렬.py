# 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름 출력하기
import sys

N = int(input())

member = []

for i in range(N):
    age, name = (sys.stdin.readline()).split() # input() 대신 sys.stdin.readline() 사용
    member.append([int(age), name, i])

member.sort(key=lambda x:(x[0], x[2]))

for j in member:
    print(j[0], j[1])
