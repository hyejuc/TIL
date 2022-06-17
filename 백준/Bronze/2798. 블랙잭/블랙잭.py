import sys

N,M=map(int,sys.stdin.readline().split())
x=sorted(list(map(int,sys.stdin.readline().split())))
m=[]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if x[i]+x[j]+x[k]>M:
                continue
            else:
                m.append(x[i]+x[j]+x[k])
print(max(m))