# 나의 코드
def solution(s):
    # str에 나타나는 숫자 중 최소값과 최대값을 찾아 반환
    List = list(map(int, s.split()))
    answer = str(min(List)) + ' ' + str(max(List))
    return answer
