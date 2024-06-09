# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    if (c%b==0) and (c%b)<=a:
        print("YES")
    else:
        print("NO")
        
