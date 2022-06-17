import sys

T=int(sys.stdin.readline())
a=[]
b=[]
for i in range(T):
    x=list(sys.stdin.readline().strip().split())
    for j in x:
        J=list(j)
        for k in range(len(J)-1,-1,-1):
            a.append(J[k])
        b.append(''.join(a))
        print(*b,end=' ')
        a=[]
        b=[]