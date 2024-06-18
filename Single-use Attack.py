# cook your dish here
import math
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    if (a==c):
        print(1)
    else:
        rem=a-c
        print(math.ceil(rem/b)+1)
