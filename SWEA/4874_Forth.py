# 문제
# SWEA 4874 - [파이썬 S/W 문제해결 기본 5일차] Stack2 - Forth

# 나의 코드
for tc in range(T):
    operand = []
    result = 0
    cal = input().split()
    for i in cal:
        if i == '.':  # 결과를 출력
            if (len(operand) > 1):
                result = "error"
            else:
                result = operand.pop()
    
        # i가 숫자일 경우
        elif i.isdigit():
            operand.append(int(i))

        # i가 연산자일 경우
        else:
            if len(operand) < 2:
                result = "error"  # 형식이 잘못되어 연산이 불가능한 경우
                break
            else: # 뺄셈, 나눗셈 주의할 것
                if i == '+':    operand.append(operand.pop() + operand.pop())
                elif i == '-':  operand.append(operand.pop(-2) - operand.pop(-1))
                elif i == '*':  operand.append(operand.pop() * operand.pop())
                elif i == '/':  operand.append(operand.pop(-2) // operand.pop(-1))

    print('#{0} {1}'.format(tc + 1, result))
