import sys

N,K=map(int,sys.stdin.readline().split())
o=[]
j=[]
for i in range(1,N+1):
    o.append(i)
x=K
while o:
    if x<=len(o):
        j.append(o.pop(x-1))
    else:
        while x>len(o):
            x -= len(o)
        j.append(o.pop(x-1))
    x += K - 1
j=list(map(str,j))
print('<'+', '.join(j)+'>')