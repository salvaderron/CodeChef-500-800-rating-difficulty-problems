n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    if (a>(b+c+d)) or (b>(a+c+d)) or (c>(b+a+d)) or (d>(b+c+a)):
        print("YES")
    else:
        print("NO")
