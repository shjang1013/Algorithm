# 신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return
import re

def solution(new_id):
    # 1. new_id의 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()

    # 2. new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    new_id = ''.join(re.findall('\w|\-|\_|\.', new_id))

    # 3. new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub('\.+', '.', new_id)

    # 4. new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id != '' and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5. new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if new_id == '':
        new_id = 'a'

    # 6. new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        # 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거 
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id