import sys

def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a
t=int(sys.stdin.readline())
for i in range(t):
    n = list(map(int,sys.stdin.readline().split()))
    res=0
    for i in range(1,len(n)):
        for j in range(i+1,len(n)):
            res+=GCD(n[i],n[j])
    print(res)