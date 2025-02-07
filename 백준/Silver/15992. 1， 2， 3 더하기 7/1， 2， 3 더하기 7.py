MOD = 1000000009

def solve():
    MAX = 1000
    
    # dp[n][m]은 n을 1, 2, 3의 합으로 m개 숫자로 만들 수 있는 방법의 수
    dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    dp[0][0] = 1 # 0을 만들기 위해 0개의 수를 사용함(한 가지 방법)

    for n in range(1, MAX + 1):
        for m in range(1, MAX + 1):
            if n >= 1:
                dp[n][m] += dp[n - 1][m - 1]
            if n >= 2:
                dp[n][m] += dp[n - 2][m - 1]
            if n >= 3:
                dp[n][m] += dp[n - 3][m - 1]
            
            dp[n][m] %= MOD

    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        print(dp[n][m])

solve()