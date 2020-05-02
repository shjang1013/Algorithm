# 나의 코드
def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        temp = str(bin(i | j))[2:] # 0b 제외
        
        if len(temp) < n:
            temp = '0'*(n-len(temp)) + temp # len(temp)의 길이와 n의 크기 맞춰주기
        
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)
    
    return answer

