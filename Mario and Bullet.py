n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    if ((b/a)>c):
        print(0)
    else:
        print(c-int(b/a))
