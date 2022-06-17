import sys

s=[False,False]+[True]*(1000000-1)
for i in range(2,int(1000000**0.5)+1):
    if s[i]:
        for j in range(2*i,len(s),i):
            s[j]=False
T=int(sys.stdin.readline())
for i in range(T):
    cnt=0
    N=int(sys.stdin.readline())
    for i in range(2,int(N/2)+1):
        if s[i] and s[N-i]:
            cnt+=1
    print(cnt)