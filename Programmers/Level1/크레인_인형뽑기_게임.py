def solution(board, moves):
    answer = 0
    
    stack = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(stack) == 0 or board[j][i-1] != stack[-1]:
                    stack.append(board[j][i - 1])
                else:
                    stack.pop()
                    answer += 1
                
                board[j][i-1] = 0
                break

    # 같은 모양 인형 두개가 없어지기 때문에 answer * 2
    return answer*2
