import sys

a=list(sys.stdin.readline().strip())
s=[]
res=''
for i in a:
    if i.isalpha():
        res+=i
    else:
        if i == '(':
            s.append(i)
        elif i == '*' or i == '/':
            while s and (s[-1]=='*' or s[-1] =='/'):
                res+=s.pop()
            s.append(i)
        elif i == '+' or i=='-':
            while s and s[-1]!='(':
                res+=s.pop()
            s.append(i)
        else:
            while s and s[-1]!='(':
                res+=s.pop()
            s.pop()
while s:
    res+=s.pop()
print(res)