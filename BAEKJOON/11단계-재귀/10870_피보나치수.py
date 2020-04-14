def Factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return Factorial(N-1) * N

print(Factorial(int(input())))
