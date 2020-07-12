# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 N개의 단어 정렬하기
import sys

N = int(input())

Word = []

for _ in range(N):
    w = sys.stdin.readline()
    if (w, len(w)) not in Word:
        Word.append((w, len(w)))

Word = sorted(Word, key=lambda x: (x[1], x[0]))

for i in Word:
    print(i[0], end='')

# 시간 단축 => 같은 단어가 입력된 경우 Word에서 찾지 말고 set 이용할 것
N = int(input())

Word = list(set(input() for _ in range(N)))

Word.sort(key=lambda x: (len(x), x))

# for문 대신 join 이용
print('\n'.join(Word))
