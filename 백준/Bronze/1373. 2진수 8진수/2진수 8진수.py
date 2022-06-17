import sys

a=list(map(int,sys.stdin.readline().strip()))
res=[]
while len(a)%3!=0:
    a.insert(0,0)
while a:
    res.append(a[-3]*4+a[-2]*2+a[-1]*1)
    a.pop()
    a.pop()
    a.pop()
res.reverse()
res=map(str,res)
print(''.join(res))