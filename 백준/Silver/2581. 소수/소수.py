M=int(input())
N=int(input())
s=list()
y=0
for i in range(M,N+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                y+=1
                break
        if y==0:
            s.append(i)
        y=0
if len(s)==0:
    print(-1)
else:
    print(sum(s))
    print(min(s))