import sys

a=list()
for i in range(1,10):
    x=int(sys.stdin.readline())
    a.append(x)
    i+=1
print(max(a))
print(a.index(max(a))+1)