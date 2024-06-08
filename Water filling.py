# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    bottle_empty=0
    if (a==0 and b==0 and c==0):
        print("Water filling time")
    elif (a==1 and b==1 and c==1):
        print("Not now")
    else:
        if a==0:
            bottle_empty+=1
        if b==0:
            bottle_empty+=1
        if c==0:
            bottle_empty+=1
        if(bottle_empty>=2):
            print("Water filling time")
        else:
            print("Not now")
