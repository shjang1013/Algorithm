# 나의 코드
def solution(s):
    s = list(s)
    s.reverse()
    
    stack = []
    stack.append(s.pop())
    
    while s:
        # stack이 비어있을 경우
        if len(stack) == 0:
            stack.append(s.pop())
        elif stack[-1] == s[-1]:
            stack.pop()
            s.pop()
        else:
            stack.append(s.pop())


    # stack에 값이 남아 있을 경우 0 반환
    answer = 0 if len(stack) != 0 else 1

    return answer
