# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    eval1=a*10
    eval2=b*5
    if eval1>eval2:
        print("FIRST")
    elif eval2>eval1:
        print("SECOND")
    else:
        print("ANY")
