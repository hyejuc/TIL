import sys
from collections import Counter

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
s=[]
res=[-1]*N
n=Counter(A)
for i in range(len(A)):
    while s and n[A[s[-1]]]<n[A[i]]:
        res[s.pop()]=A[i]
    s.append(i)
print(*res)