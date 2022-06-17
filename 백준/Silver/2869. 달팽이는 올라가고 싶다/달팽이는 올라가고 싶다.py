import math
import sys

A,B,V=map(int,sys.stdin.readline().split())
d=math.ceil((V-A)/(A-B))+1
print(d)