# 처음 풀이
def solution(phone_book):
    answer = False
    
    for num in phone_book:
        for i in phone_book:
            if num in i[0:len(num)] and num != i:
                return answer

    answer = True
    return answer


# 다른 풀이
def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False

    return answer
