# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    if b>c:
        print(0)
    elif ((a*b)<c):
        print(a)
    else:
        print((c//b))
