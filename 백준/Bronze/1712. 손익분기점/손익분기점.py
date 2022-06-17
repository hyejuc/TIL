import sys

A,B,C=map(int,sys.stdin.readline().split())
if C-B==0:
    print(-1)
else:
    N=(A/(C-B))+1
    if N>0:
        print(int(N))
    else:
        print(-1)