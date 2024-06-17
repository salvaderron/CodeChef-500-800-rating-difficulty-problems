# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    minion=[]
    count=0
    minion=list(map(int,input().split()))
    for j in range(0,len(minion)):
        minion[j]=minion[j]+b
    for j in range(0,len(minion)):
        if (minion[j]%7==0):
            count+=1
    print(count)
