import sys

N=int(sys.stdin.readline())
ans=0
i=len(str(N))-1
a=0
while i>=0:
    if a==0:
        if N>=10**i:
            ans+=((N-10**i)+1)*(i+1)
            i-=1
            a=1
        else:
            i-=1
    else:
        if N>=10**i:
            ans+=(9*10**i)*(i+1)
            i-=1
print(ans)