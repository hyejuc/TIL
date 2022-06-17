import sys

N=int(sys.stdin.readline())
cost=[]
for i in range(N):
    cost.append(list(map(int,sys.stdin.readline().split())))
dp=[cost[0]]+[[0]*3 for i in range(N-1)]
for i in range(1,N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
print(min(dp[N-1]))