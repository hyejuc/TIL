import sys

N=sys.stdin.readline()
X=list(map(int,sys.stdin.readline().split()))
x=sorted(list(set(X)))
d={x[i]: i for i in range(len(x))}
for i in X:
    print(d[i],end=' ')