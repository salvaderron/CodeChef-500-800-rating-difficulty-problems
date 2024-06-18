# cook your dish here
x=int(input())
for i in range(0,x):
    n=int(input())
    arr=list(map(int,input().split()))
    if (n%2!=0):
        print(-1)
    else:
        one=arr.count(1)
        minus=arr.count(-1)
        print(abs(one-minus)//2)
            
    
