def t(n):
    A = [0] * (n + 1)
    A[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            A[i] += A[j] * A[i - 1 - j]
    
    return A[n]

n = int(input().strip())
print(t(n))
