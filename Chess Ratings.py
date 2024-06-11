# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    count=0
    if (a==b):
        print(0)
    else:
        while(b>a):
            a+=8
            count+=1
        print(count)
