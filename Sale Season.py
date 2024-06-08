# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    if x<=100:
        print(x)
    elif x>100 and x<=1000:
        print(x-25)
    elif x>1000 and x<=5000:
        print(x-100)
    else:
        print(x-500)
