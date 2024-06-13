# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    time=0
    for j in range(1,a+1):
        if (j%2==0):
            time=time+b
        else:
            time=time+c
    print(time)
            
