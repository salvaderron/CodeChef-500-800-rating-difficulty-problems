# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    app=(b/a)*100
    if app>=50:
        print("YES")
    else:
        print("NO")
