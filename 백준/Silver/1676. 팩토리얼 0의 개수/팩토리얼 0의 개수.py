import sys

N=int(sys.stdin.readline())
f=1
res=0
for i in range(1,N+1):
    f*=i
for i in reversed(list(str(f))):
    if i == '0':
        res+=1
    else:
        break
print(res)