n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    need=b*2
    if (a<need):
        print(0)
    else:
        print(int(a/need))
