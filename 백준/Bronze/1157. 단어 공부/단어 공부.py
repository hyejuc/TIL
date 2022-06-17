import sys
s=list(sys.stdin.readline())
A=[0 for i in range(26)]
a=[0 for i in range(26)]
for i in range(26):
    if chr(65+i) in s:
        del A[i]
        A.insert(i,s.count(chr(65+i)))
    if chr(97+i) in s:
        del a[i]
        a.insert(i, s.count(chr(97+i)))
    i+=1
X=[x+y for x,y in zip(A,a)]
x=sorted(X)
x.reverse()
n=x.count(x[0])
if n>1:
    print('?')
else:
    print(chr(X.index(max(X))+65))