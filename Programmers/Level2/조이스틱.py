# 수정한 코드
def solution(name):
    answer = 0
    name = list(name)
    i = 0
    base = ['A'] * len(name)
    
    while True:
        right = 1
        left = 1
        
        if name[i] != 'A':
            answer += min(ord(name[i]) - ord('A'), (ord('Z') - ord(name[i]) + 1))
            name[i] = 'A'
        
        if name == base:
            break
    
        for j in range(1, len(name)):
            if name[i+j] == 'A': # 오른쪽
                right += 1
            else:
                break
            
            if name[i-j] == 'A': # 왼쪽
                left += 1
            else:
                break
        
        
        answer += left if right > left else right
        i += -left if right > left else right
                        
    return answer

# 차근차근 한 줄 씩 작성하기
1. 조건 제대로 확인하기 => 위, 아래 뿐만 아니라 왼쪽, 오른쪽 조이스틱의 움직임 확인하기
2. 'A'의 개수가 적은 쪽 찾기 => 왼쪽, 오른쪽 따로 나눠 접근하기

