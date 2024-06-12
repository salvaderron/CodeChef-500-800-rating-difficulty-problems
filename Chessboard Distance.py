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

# Can also be done using abs() function in python

# cook your dish here
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split(" "))
    if abs(x1-x2)>abs(y1-y2):
        print(abs(x1-x2))
    else:
        print(abs(y1-y2))
