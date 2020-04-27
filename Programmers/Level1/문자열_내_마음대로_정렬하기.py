def solution(strings, n):
    strings.sort()
    
    # 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하기
    return sorted(strings, key=lambda x:x[n])
