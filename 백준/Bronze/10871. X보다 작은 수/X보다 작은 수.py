import sys

N,X=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
a=list()
i=0
for i in range(len(A)):
    if A[i]<X:
        a.append(A[i])
    i+=1
print(*a)