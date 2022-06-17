import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
dp=[a[0]]
for i in range(1,len(a)):
    dp.append(max(dp[i-1]+a[i],a[i]))
print(max(dp))