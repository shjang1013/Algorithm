# 나의 코드
def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif len(stack) == 0:
            stack.append(i)
            break
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                break

    answer = True if len(stack) == 0 else False

    return answer
