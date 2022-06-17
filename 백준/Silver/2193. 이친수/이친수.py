import sys

dp=[[0,1]]
for i in range(1,90+1):
    dp.append([sum(dp[i-1]),dp[i-1][0]])
N=int(sys.stdin.readline())
print(sum(dp[N-1]))