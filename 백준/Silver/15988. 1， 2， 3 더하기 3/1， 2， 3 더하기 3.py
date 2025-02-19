var1 = 1000000009

def dp_func(max_num):
    dp = [0] * (max_num + 1) 
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, max_num + 1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % var1

    return dp  
T = int(input())
cases = [int(input()) for i in range(T)]

max_num = max(cases)  # 입력 값 중 가장 큰 값
dp = dp_func(max_num) 

for n in cases:
    print(dp[n])