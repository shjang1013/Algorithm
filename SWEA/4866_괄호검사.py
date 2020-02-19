# 문제
# SWEA 4866 - [파이썬 S/W 문제해결 기본 4일차] Stack1 - 괄호검사

# 나의 코드(오답) - 테스트케이스가 바뀌었음에도 불구하고 stack은 초기화되지 않아 오답...
T = int(input())

bracket_dic = {']':'[', '}':'{', ')':'('}

stack = []

for tc in range(T):
    line = input()
    for i in line:
        # 여는 괄호가 올 경우
        if i in bracket_dic.values():
            stack.append(i)
        # 닫는 괄호가 올 경우
        elif i in bracket_dic:
            # stack이 비어있을 경우
            if len(stack) == 0:
                stack = [i]
                break
            # stack에 저장된 괄호와 일치하지 않는 경우
            elif bracket_dic.get(i) != stack[-1]:
                break
            else:
                stack.pop()

    if not len(stack):
        result = 1
    else:
        result = 0

    print("#%d %d" % (tc+1, result))

# 정답
T = int(input())

bracket_dic = {'}':'{', ')':'('}

for tc in range(T):
    stack = []
    line = input()
    for i in line:
        # 여는 괄호가 올 경우
        if i in bracket_dic.values():
            stack.append(i)
        # 닫는 괄호가 올 경우
        elif i in bracket_dic:
            # stack이 비어있을 경우
            if len(stack) == 0:
                stack = [i]
                break
            # stack에 저장된 괄호와 일치하지 않는 경우
            elif bracket_dic.get(i) != stack[-1]:
                break
            else:
                stack.pop()

    if not len(stack):
        result = 1
    else:
        result = 0

    print("#%d %d" % (tc+1, result))


