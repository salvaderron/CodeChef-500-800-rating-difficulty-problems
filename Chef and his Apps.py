# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    mem_left=a-(b+c)
    if mem_left>=d:
        print(0)
    else:
        if ((b+mem_left)>=d or (c+mem_left)>=d):
            print(1)
        else:
            print(2)
