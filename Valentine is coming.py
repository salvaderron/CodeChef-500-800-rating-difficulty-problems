# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if b>a:
        print(0)
    else:
        print(int(a/b))
