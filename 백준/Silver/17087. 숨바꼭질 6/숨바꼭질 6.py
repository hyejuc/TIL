import sys

def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a
N,S=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
D=[]
for i in A:
    D.append(abs(S-i))
D=list(set(D))
x=D[0]
for i in D:
    x = GCD(x,i)
print(x)