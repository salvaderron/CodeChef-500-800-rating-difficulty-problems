# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    if ((b*3)-((a-b)*1)) >= c:
        print("PASS")
    else:
        print("FAIL")
