# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if (a+b)>=11:
        print(21-(a+b))
    else:
        print(-1)
