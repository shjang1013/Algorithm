# input()는 시간초과 발생할 수도 있음 => sys.stdin.readline() 사용
import sys

while True:
    stack = []
    bracket = sys.stdin.readline().rstrip()
    if bracket == '.':
        break
    
    for i in bracket:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0:
                stack.append(i)
                break
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            else:
                break

    print("no") if len(stack) != 0 else print("yes")


# 다른 풀이(정규식 이용)
import re

regex = r'[()\[\]]'

while True:
    string = input()
    if string == '.':
        break
    temp = ''.join(re.findall(regex, string))

    for _ in range(len(temp)//2):
        temp = temp.replace('()', '')
        temp = temp.replace('[]', '')

    if len(temp) == 0:
        print('yes')
    else:
        print('no')
