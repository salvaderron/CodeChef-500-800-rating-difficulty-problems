# cook your dish here
n=int(input())
for i in range(0,n):
    a=int(input())
    if a%5 !=0:
        print(-1)
    else:
        if a%10 == 0:
            print(a//10)
        else:
            print((a//10)+1)
        
