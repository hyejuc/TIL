import sys

n=int(sys.stdin.readline().strip())
a=1
s=[]
res=[]
b=True
for i in range(n):
    x=int(sys.stdin.readline().strip())
    while a<=x:
        s.append(a)
        res.append('+')
        a+=1
    if s[-1]==x:
        s.pop()
        res.append('-')
    else:
        b=False
if b==False:
    print('NO')
else:
    for i in res:
        print(i)