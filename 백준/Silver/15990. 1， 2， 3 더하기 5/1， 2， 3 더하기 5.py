import sys

dp = [[0,0,0],[1,0,0],[0,1,0],[1,1,1]]
for j in range(4, 100000 + 1):
    dp.append([(sum(dp[j - 1]) - dp[j - 1][0])%1000000009, (sum(dp[j - 2]) - dp[j - 2][1])%1000000009, (sum(dp[j - 3]) - dp[j - 3][2])%1000000009])
T=int(sys.stdin.readline())
for i in range(T):
    n=int(sys.stdin.readline())
    print(sum(dp[n])%1000000009)