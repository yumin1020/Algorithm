def my_func(A):
    N = len(A)
    dp = A[:]
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + A[i])
    return max(dp)

N = int(input())
A = list(map(int, input().split()))
print(my_func(A))