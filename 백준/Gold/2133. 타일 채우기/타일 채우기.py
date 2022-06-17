import sys

N=int(sys.stdin.readline())
if (3*N)%2!=0:
    print(0)
else:
    dp = [3]
    for i in range(1,int(N/2)):
        dp.append(dp[i-1]*3)
        dp[i]+=2
        if i>1:
            for j in range(i-1):
                dp[i] += dp[j] * 2
    print(dp[-1])