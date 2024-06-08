# cook your dish here
import math
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if (b>=a):
        print(0)
    else:
        want=a-b
        print(math.ceil(want/4))
