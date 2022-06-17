import sys

def count2(n):
    res=0
    while n!=0:
        n//=2
        res+=n
    return res
def count5(n):
    res=0
    while n!=0:
        n//=5
        res+=n
    return res
n,m=map(int,sys.stdin.readline().split())
print(min(count2(n)-count2(n-m)-count2(m),count5(n)-count5(n-m)-count5(m)))