X=int(input())
f=1
cnt=1
while X>f:
    cnt+=1
    f+=cnt
gap=X-f+cnt
if cnt%2==0:
    top=gap
    bottom=cnt+1-top
else:
    bottom=gap
    top=cnt+1-bottom
print(f'{top}/{bottom}')