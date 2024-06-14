# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    ans=1
    for j in range(0,2):
        ans=ans*x
        x-=1
    print(ans)
