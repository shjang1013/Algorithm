score = []

for i in range(1,9):
    score.append((i, int(input())))

score = sorted(score, key=lambda x:x[1], reverse=True)

question = []
sum = 0
for i in score[:5]:
    sum += i[1]
    question.append(i[0])

# 참가자의 총점
print(sum)
# 어떤 문제가 최종 점수에 포함되는지를 공백으로 구분하여 출력하기
print(' '.join(map(str, sorted(question))))
