# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    count = 0
    for day in range(1, x + 1):
        if day % 7 == 2:
            count += 1
    print(count)
        
