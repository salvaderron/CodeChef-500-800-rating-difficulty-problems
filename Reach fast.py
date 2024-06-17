# cook your dish here
import math
n=int(input())
for i in range(0,n):
    a,b,k=map(int,input().split())
    if a==b:
        print(0)
    else:
        print(math.ceil(abs(a-b)/k))
