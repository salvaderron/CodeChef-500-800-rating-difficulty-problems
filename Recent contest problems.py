# cook your dish here
n=int(input())
arr=[]
for i in range(0,n):
    x=int(input())
    s=0
    l=0
    arr=list(map(str,input().split()))
    s=arr.count("START38")
    l=arr.count("LTIME108")
    print(s,l)
    
