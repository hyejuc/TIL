import sys

N,B=sys.stdin.readline().split()
a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res=0
n=0
N=N[::-1]
for i in N:
    res+=a.find(i)*(int(B)**n)
    n+=1
print(res)