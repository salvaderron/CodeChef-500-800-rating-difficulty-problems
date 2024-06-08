# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,x,y=map(int,input().split())
    if (a*b)<=(x*y):
        print("Yes")
    else:
        print("No")
