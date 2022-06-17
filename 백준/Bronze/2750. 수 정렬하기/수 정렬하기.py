N=int(input())
a=list()
for i in range(N):
    x=int(input())
    a.append(x)
a.sort()
print(*a,sep='\n')