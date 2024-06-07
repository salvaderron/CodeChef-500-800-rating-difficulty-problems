# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    x=(c/(a*b))*100
    if x>50:
        print("YES")
    else:
        print("NO")
