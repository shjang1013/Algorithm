# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력하기 
count = 0

word = input()

for i in range(len(word)):
    count += 1
    if word[i] == '=':
        if i-1 != 0 and word[i-1] == 'z' and word[i-2] == 'd':
            count -= 2
        else:
            count -= 1
    elif word[i] == '-':
        count -= 1
    elif word[i] == 'j':
        if i != 0 and (word[i-1] == 'l' or word[i-1] == 'n'):
            count -= 1

print(count)

# 다른 코드
List = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

for i in List:
    word = word.replace(i,'o')

print(len(word))

# 문자열 함수 공부하기
문자 개수 세기(count), 위치 알려주기1(find), 위치 알려주기2(index), 문자열 삽입(join), 소문자를 대문자로 바꾸기(upper), 대문자를 소문자로 바꾸기(lower), 양쪽 공백 지우기(strip), 문자열 바꾸기(replace), 문자열 나누기(split)
