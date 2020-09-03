# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 출력하기 
N = input()

NUM = []

ALPA = ""

for i in N:
    if i.isdigit():
        NUM.append(int(i))
    else:
        ALPA += i

print(''.join(sorted(ALPA))+str(sum(NUM)))
