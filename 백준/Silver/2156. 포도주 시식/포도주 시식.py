import sys

n=int(sys.stdin.readline())
w=[]
for i in range(n):
    w.append(int(sys.stdin.readline()))
dp=[w[0]]
for i in range(1,n):
    if i==1:
        dp.append(w[0]+w[1])
    elif i==2:
        dp.append(max(dp[i-1],w[i-1]+w[i],dp[i-2]+w[i]))
    else:
        dp.append(max(dp[i-1],dp[i-3]+w[i-1]+w[i],dp[i-2]+w[i]))
print(dp[n-1])