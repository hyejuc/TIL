import sys
from collections import deque

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
d=deque()
NGE=[-1]*N
for i in range(len(A)):
    while d and A[d[-1]]<A[i]:
        NGE[d.pop()]=A[i]
    d.append(i)
print(*NGE)