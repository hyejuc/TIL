import sys

N,M=map(int,sys.stdin.readline().split())
c=[]
cnt=[]
for i in range(N):
    c.append(list(sys.stdin.readline().strip()))

for i in range(0,N-7):
    for j in range(0,M-7):
        b=0
        w=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if c[k][l]!='B':
                        b+=1
                    elif c[k][l]!='W':
                        w+=1
                else:
                    if c[k][l]!='W':
                        b+=1
                    else:
                        w+=1
        cnt.append(b)
        cnt.append(w)
print(min(cnt))