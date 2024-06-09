n=int(input())
for i in range(0,n):
    a=int(input())
    if (a<=4):
        print(1)
    elif (a%4 ==0):
        print(int(a/4))
    else:
        print(int((a//4)+1))
    
