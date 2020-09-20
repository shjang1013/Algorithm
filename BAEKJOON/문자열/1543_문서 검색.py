# 중복되지 않게 최대 몇 번 등장하는지 출력하기
import sys

# 입력받기
document = sys.stdin.readline().rstrip()

word = sys.stdin.readline().rstrip()

document = document.replace(word, '!')

print(document.count('!'))
