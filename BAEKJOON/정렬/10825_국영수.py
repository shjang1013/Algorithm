# 국어 점수가 감소, 영어 점수가 증가, 수학 점수가 감소, 이름이 사전 순으로 증가하는 순서로 정렬 
import sys

N = int(input())

student = []

for _ in range(N):
    name, kor, eng, mat = sys.stdin.readline().split()
    student.append([name, int(kor), int(eng), int(mat)])

sorted_student = sorted(student, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in sorted_student:
    print(i[0])
