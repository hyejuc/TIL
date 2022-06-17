N=int(input())
A=list()
B=list()
max_a=N//3
for a in range(max_a+1):
    if (N-3*a)%5==0:
        A.append(a)
        B.append((N-3*a)//5)
    else:
        continue
X=[x+y for x,y in zip(A,B)]
if len(X)==0:
    print(-1)
else:
    print(min(X))