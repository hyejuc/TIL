import sys

N=int(sys.stdin.readline())
n=list(map(int,sys.stdin.readline().split()))
s=0
y=0
for i in range(N):
    if n[i]>1:
        for j in range(2,max(n)+1):
            if n[i]%j==0:
                    y+=1
        if y==1:
            s+=1
        y=0
print(s)