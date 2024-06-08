# cook your dish here
n=int(input())
for i in range(0,n):
    a=int(input())
    sell=a*50
    bsug=0.2*sell
    sam=0.2*sell
    rent=(3/10)*sell
    print(int(sell-(bsug+sam+rent)))
