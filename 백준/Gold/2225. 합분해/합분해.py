import sys

N,K=map(int,sys.stdin.readline().split())
dp=[[0]*N for i in range(K)]
for i in range(N):
    dp[0][i]+=1
for i in range(1,K):
    for j in range(N):
        if j==0:
            dp[i][j]=(i+1)%1000000000
        else:
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000000
print(dp[K-1][N-1]%1000000000)