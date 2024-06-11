# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    a=input()
    ans=""
    for j in range(0,x):
        temp=a[j]
        if (temp=='A'):
            ans=ans+'T'
        elif (temp=='T'):
            ans=ans+'A'
        elif (temp=='C'):
            ans=ans+'G'
        elif (temp=='G'):
            ans=ans+'C'
    print(ans)
            
