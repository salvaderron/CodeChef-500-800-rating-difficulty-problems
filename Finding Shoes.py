n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if b>=a:
        print(a)
    else:
        print(2*a-b)
        
