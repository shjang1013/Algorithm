# 완전 탐색 
def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        String = []
        for j in range(0, len(s), i):
            String.append(s[j:j + i])
        
        l = ""
        same = 1
        for j in range(len(String) - 1):
            if String[j] == String[j + 1]:
                same += 1
            else:
                l += String[j] if same == 1 else str(same) + String[j]
                
                same = 1
    
        # 남아있는 문자열 처리
        l += String[-1] if same == 1 else str(same) + String[-1]
        
        answer = min(answer, len(l))

    return answer

# 메모
1. 문자열 개수별로 자르기
for j in range(0, len(s), i):
    String.append(s[j:j + i])

2. 예외사항 꼼꼼하게 확인하기 => 예) s = 'a'
