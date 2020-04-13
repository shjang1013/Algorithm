def sum(B):
    sum = 0
    for i in B:
        sum += int(i)
    
    return sum

A = input()
B = input()

print(sum(B))
