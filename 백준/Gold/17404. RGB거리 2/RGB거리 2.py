import sys

N=int(sys.stdin.readline())
c=[]
for i in range(N):
    c.append(list(map(int,sys.stdin.readline().split())))
inf=10**7
res=10**7
for i in range(3):
    dp=[[inf]*3 for i in range(N)]
    dp[0][i]=c[0][i]
    for j in range(1,N):
        dp[j][0]=min(dp[j - 1][1], dp[j - 1][2]) + c[j][0]
        dp[j][1]=min(dp[j - 1][0], dp[j - 1][2]) + c[j][1]
        dp[j][2]=min(dp[j - 1][0], dp[j - 1][1]) + c[j][2]
    for j in range(3):
        if i!=j:
            res=min(res,dp[-1][j])
print(res)