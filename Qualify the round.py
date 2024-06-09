# cook your dish here
n=int(input())
for i in range(0,n):
    q,a,b=map(int,input().split())
    if ((a*1)+(b*2))>=q:
        print("Qualify")
    else:
        print("NotQualify")
