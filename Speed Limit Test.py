# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    s1=a/b
    s2=c/d
    if s1>s2:
        print("Alice")
    elif s2>s1:
        print("Bob")
    else:
        print("Equal")
