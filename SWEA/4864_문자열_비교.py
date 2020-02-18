# 문제
# SWEA 4864 - [파이썬 S/W 문제해결 기본 3일차] STRING - 문자열 비교

# 나의 코드(제한시간 초과)
def makeSkipList(pat):
    return [pat[len(pat)-i-1] for i in range(len(pat))]

def booyerMoore(txt, skip):
    i = len(skip)-1
    s = 0
    t = 0
    while i <= len(txt):
        if txt[i] == skip[s]:
            i = i-1
            s = s+1
            if s == len(skip)-1:
                return s
        else:
            if txt[i] in skip:
                i = i + skip.index(txt[i])
            else:
                i = i + len(skip)
            
            if i > len(txt) - 1:
                break
    return t


T = int(input())

for tc in range(T):
    pat = input()
    txt = input()
    
    skipList = makeSkipList(pat)
    count = booyerMoore(txt, skipList)
    
    if count > 0:
        count = 1
    
    print('#{0} {1}' .format(tc+1, count))

# 수정한 코드(다른 코드 참고) - 너무 복잡하게 생각하지 말 것
T = int(input())

for tc in range(T):
    pat = input()
    txt = input()
    
    result = 0
    for i in range(len(txt)-len(pat)+1):
        if txt[i:i+len(pat)]==pat:
            result = 1

    print('#{0} {1}' .format(tc+1, result))
