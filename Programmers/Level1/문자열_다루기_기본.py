def solution(s):
    answer = False
    if (len(s) == 4 or len(s) == 6) and s.isdecimal():
        answer = True
    return answer
