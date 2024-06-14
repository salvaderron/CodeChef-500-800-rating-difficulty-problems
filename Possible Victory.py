# cook your dish here
r,o,c=map(int,input().split())
over_remain=20-o
run=(over_remain*6)*6
if (c+run)>r:
    print("YES")
else:
    print("NO")
