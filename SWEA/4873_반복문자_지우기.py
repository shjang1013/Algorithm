# 문제
# SWEA 4873 - [파이썬 S/W 문제해결 기본 4일차] Stack1 - 반복문자 지우기

# 나의 코드
T = int(input())

for tc in range(T):
    # 스택
    stack = []
    line = input()
    for i in range(len(line)):
        # 스택이 비었거나, 스택의 마지막 값과 i가 같지 않은 경우
        if not stack or stack[-1] != line[i]:
            stack.append(line[i])
        # 스택의 마지막 값과 i가 같은 경우
        else:
            stack.pop()

print("#%d %d" %(tc+1,len(stack)))
