# cook your dish here
n=int(input())
a=list(map(int,input().split()))
ecount=0
ocount=0
for i in range(0,n):
    if (a[i] % 2)==0:
        ecount=ecount+1
    else:
        ocount=ocount+1
if (ecount>ocount):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
    
