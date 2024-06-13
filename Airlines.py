# cook your dish here
import math
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    need=math.ceil(b/100)
    if a>=need:
        print(0)
    else:
        print(abs(need-a))
