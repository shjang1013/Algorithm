# 문제
# SWEA 4865 - [파이썬 S/W 문제해결 기본 3일차] STRING - 글자수

# 나의 코드
T = int(input())

for tc in range(T):
    # 딕셔너리 초기화
    dic = {}
    
    N = input()
    # 문자열의 각 문자를 딕셔너리에 추가
    for n in N:
        dic[n] = 0
    
    M = input()
    # 문자열의 각 문자가 딕셔너리 key에 포함될 경우
    for m in M:
        if m in list(dic.keys()):
            dic[m] = dic.get(m) + 1  # key에 해당하는 value에 1 더하기

    # 딕셔너리 value 중에서 최댓값 찾기
    print('#{0} {1}' .format(tc+1, max(dic.values())))
