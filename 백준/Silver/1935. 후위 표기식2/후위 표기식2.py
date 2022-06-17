import sys

N=int(sys.stdin.readline())
s=list(sys.stdin.readline().strip())
n=[]
res=0
num=[]
dic={}
for i in sorted(list(set(s))):
    if i != '*' and i!='+' and i!='/' and i!='-':
        num.append(i)
for i in num:
    dic[i]=int(sys.stdin.readline().strip())
while s:
    if s[0] == '*' or s[0]=='+' or s[0]=='/' or s[0]=='-':
        if s[0] =='+':
            res=n.pop()+n.pop()
        elif s[0]=='*':
            res=n.pop()*n.pop()
        elif s[0]=='/':
            res=1/(n.pop()/n.pop())
        else:
            res=0-n.pop()+n.pop()
        n.append(res)
        s.pop(0)
    else:
        n.append(dic.get(s.pop(0)))
print(format(res,'.2f'))