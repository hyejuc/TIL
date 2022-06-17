import sys
T=int(sys.stdin.readline())
for i in range(T):
    M,N,x,y=map(int,sys.stdin.readline().split())
    k=-1
    while x<=M*N:
        if (x-y)%N==0:
            k=x
            break
        x+=M
    print(k)