def solve(num):
    count = 0
    
    # 한자리수 or 두자리수 : 각 자리 수가 등차수열을 이룬다.
    if num < 100:
        count = num
    
    # 세자리수 or 1000
    else:
        for i in range(100, num+1):
            i = str(i)
            if (int(i[0])-int(i[1])) == (int(i[1])-int(i[2])):
                count+=1
        count = 99+count
    print(count)

solve(int(input()))
