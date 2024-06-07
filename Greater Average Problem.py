# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    if ((a+b)/2)>c:
        print("YES")
    else:
        print("NO")
