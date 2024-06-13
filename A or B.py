# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    a1=500-(a*2)
    a2=1000-((a+b)*4)
    ax=a1+a2
    b1=1000-(b*4)
    b2=500-((a+b)*2)
    bx=b1+b2
    if ax>=bx:
        print(ax)
    else:
        print(bx)
    
