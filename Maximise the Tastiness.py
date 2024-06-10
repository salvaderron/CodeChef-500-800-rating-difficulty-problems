n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    print(max(a,b)+max(c,d))
