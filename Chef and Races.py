# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    if (a==c or a==d) and (b==c or b==d):
        print(0)
    elif (a==c or a==d or b==c or b==d):
        print(1)
    else:
        print(2)
