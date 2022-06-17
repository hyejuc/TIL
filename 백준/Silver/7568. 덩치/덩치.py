import sys

N=int(sys.stdin.readline())
a=[]
r=[1]*N
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    a.append([x,y])
for i in range(N):
    for j in range(N):
        if a[i][0]<a[j][0]:
            if a[i][1]<a[j][1]:
                r[i]+=1
print(*r)