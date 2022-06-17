import sys

T=int(sys.stdin.readline())
a=0
for i in range(T):
    x=list(sys.stdin.readline().strip())
    for j in range(len(x)):
        if len(x)%2!=0:
            a-=1
            break
        elif x[j]=='(':
            a+=1
        elif x[j]==')':
            a-=1
        if a<0:
            break
    if a==0:
        print('YES')
    else:
        print('NO')
    a=0