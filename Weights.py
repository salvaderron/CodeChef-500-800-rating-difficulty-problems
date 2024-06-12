# cook your dish here
n=int(input())
for i in range(0,n):
    x,b,c,d=map(int,input().split())
    if (((b+c)==x)or((b+d)==x)or((c+d)==x)or((b+c+d)==x)or(b==x)or(c==x)or(d==x)):
        print("YES")
    else:
        print("NO")
