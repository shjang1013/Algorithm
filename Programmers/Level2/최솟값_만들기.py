# 나의 코드
def solution(A,B):
    answer = 0
    
    A.sort(reverse = True)
    B.sort()
    
    # A의 최솟값과 B의 최댓값 곱하기 
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer
