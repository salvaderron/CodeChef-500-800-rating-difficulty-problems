# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    d1=a-c
    d2=b-d
    if d1<0:
        d1=-1*d1
    if d2<0:
        d2=-1*d2
    print(max(d1,d2))
