# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    if (a==b):
        print("YES")
    else:
        if(b>a):
            diff=b-a
            if(c>=diff):
                print("YES")
            else:
                print("NO")
        elif (a>b):
            diff=a-b
            if (d>=diff):
                print("YES")
            else:
                print("NO")
                
