import sys

dp=[[0,1,1,1,1,1,1,1,1,1]]
for i in range(1,100+1):
    temp=[]
    for j in range(10):
        if j==0:
            temp.append(dp[i-1][1])
        elif j==9:
            temp.append(dp[i-1][8])
        else:
            temp.append(dp[i-1][j-1]+dp[i-1][j+1])
    dp.append(temp)
N=int(sys.stdin.readline())
print(sum(dp[N-1])%1000000000)