import sys
x=sys.stdin.readline()
n=0
C=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in C:
    if i in x:
        n+=x.count(i)
        x=x.replace(i,".")
x=x.replace('.',"").strip()
print(len(x)+n)