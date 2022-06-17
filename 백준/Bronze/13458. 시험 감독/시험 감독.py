import math
import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
b,c=map(int,sys.stdin.readline().split())
s=n
for i in range(n):
    if a[i]-b>0:
        s+=math.ceil((a[i]-b)/c)
print(s)