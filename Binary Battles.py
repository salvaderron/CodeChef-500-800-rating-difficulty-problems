# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    time=0
    while(a!=1):
        time=time+b+c
        a=int(a/2)
    print(time-c)
