n=int(input())
for i in range(0,n):
    x=int(input())
    arr=list(map(int,input().split()))
    count=0
    for k in range(0,len(arr)):
        if (arr[k]>=1000):
            count+=1
    print(count)
