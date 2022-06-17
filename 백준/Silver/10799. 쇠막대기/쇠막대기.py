import sys

s=list(sys.stdin.readline().strip())
st=[]
res=0

for i in range(len(s)):
    if s[i]=='(':
        if i==len(s)-1:
            break
        elif s[i+1]==')':
            res+=len(st)
        else:
            st.append(1)
    else:
        if s[i-1]=='(':
            pass
        else:
            st.pop()
            res+=1
print(res)