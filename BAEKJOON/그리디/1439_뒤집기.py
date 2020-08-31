# 문자열 S가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하기
S = input()

List = []

s = S[0]

count = 0

for i in S[1:]:
    if s[-1] != i:
        List.append(s)
        s = i
    else:
        s += i

# 마지막 문자열 삽입
List.append(s)

for i in List:
    if '1' in i:
        count += 1

# 최소 횟수 출력
print(min(count, len(List)-count))


# 다른 코드
S = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if S[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if S[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))
