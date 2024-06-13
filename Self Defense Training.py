# cook your dish here
n=int(input())
age=[]
for i in range(0,n):
    x=int(input())
    age=list(map(int,input().split()))
    count=0
    for j in range(0,len(age)):
        if (age[j]>=10 and age[j]<=60):
            count+=1
    print(count)
