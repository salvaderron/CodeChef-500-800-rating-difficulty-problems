# cook your dish here
n=int(input())
for i in range(0,n):
    people=[]
    count=0
    total_people,age_limit=map(int,input().split())
    people=list(map(int,input().split()))
    for j in range(0,len(people)):
        if people[j]>=age_limit:
            count+=1
    print(count)
