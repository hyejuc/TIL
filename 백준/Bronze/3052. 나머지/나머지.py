import sys

a=list()
for i in range(1,11):
    x=int(sys.stdin.readline())%42
    if x in a:
        i+=1
        continue
    else:
        a.append(x)
print(len(a))