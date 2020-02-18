# 문제
# SWEA 4861 - [파이썬 S/W 문제해결 기본 3일차] STRING - 회문

# 수정한 코드(다른 코드 참고) - 문제 제대로 읽자..!
T = int(input())

for tc in range(T):
    # NxN 크기의 글자판, M 길이의 회문
    N, M = map(int, input().split())
    result = []
    
    # 가로
    horizon_list = []
    for i in range(N):
        data = input()
        horizon_list.append(data)
        
        # 가로줄에서 회문 찾기
        for j in range(N-M+1):
            if data[j:j+M] == ''.join(reversed(data[j:j+M])):
                result.append(data[j:j+M])

    # 세로
    vertical_list = []
    for i in range(N):
        vertical_str = ''
        for str1 in horizon_list:
            vertical_str += str1[i]
        vertical_list.append(vertical_str)

    # 세로줄에서 회문 찾기
    for vertical_data in vertical_list:
        for i in range(N-M+1):
            if vertical_data[i:i+M] == ''.join(reversed(vertical_data[i:i+M])):
                result.append(vertical_data[i:i+M])


    print('#%d %s' %(tc+1, result[0])


# 회문의 방법
# 1. 반복문으로 문자 검사하기
word = input('input : ')
          
is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):     # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:     # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
          is_palindrome = False      # 회문이 아님
          break
          
print(is_palindrome)                # 회문 판별값 출력
        
# 2. 시퀀스 뒤집기로 문자검사하기
word = input('input : ')
          
print(word == word[::-1])    # 원래 문자열과 반대로 뒤집은 문자열을 비교

# 3. list와 reversed 사용하기
word = input('input : ')
          
if list(word) == list(reversed(word)) # reversed는 reversed 객체를 반환하기 때문에 list로 만들어야함
    is_palindrome = True
          
# 4. 문자열의 join 메서드와 reversed 사용하기
word = input('input : ')
          
if word == ''.join(reversed(word))
    is_palindrome = True
          
# 참고 블로그
https://scarletbreeze.github.io/articles/2019-07/SWE(4861)%ED%9A%8C%EB%AC%B8
        
