def solution(s):
    # 리스트를 문자열로 바꾸는 방법 : ''.join(list)
    return ''.join(sorted(s, reverse=True))
