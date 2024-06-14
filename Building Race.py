# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    if ((a/b)==(c/d)):
        print("Both")
    elif ((a/b)>(c/d)):
        print("Chefina")
    else:
        print("Chef")
