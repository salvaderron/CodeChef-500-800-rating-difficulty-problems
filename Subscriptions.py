# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if (a%6==0):
        print((a//6)*b)
    else:
        print(((a//6)+1)*b)
    
