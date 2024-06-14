# cook your dish here
import math
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    print(math.ceil((a+(c/30))/b))
