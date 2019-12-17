A,B,C = map(int, input().split())

if A>=B:
    if A>=C:
        if B>=C:
            print(B)
        else:
            print(C)
    else:
        print(A)

else:
    if B>=C:
        if A>=C:
            print(A)
        else:
            print(C)
    else:
        print(B)

# thrList = list(map(int, input().split()))
# thrList.sort()
# print(thrList[1])
