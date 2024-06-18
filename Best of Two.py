# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d,e,f=map(int,input().split())
    amax=a+b+c-min(a,b,c)
    bmax=d+e+f-min(d,e,f)
    if (amax>bmax):
        print("Alice")
    elif (bmax>amax):
        print("Bob")
    else:
        print("Tie")
