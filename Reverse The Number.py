n=int(input())
for i in range(0,n):
    num=0
    x=int(input())
    while x>0:
        num=(num*10)+(x%10)
        x//=10
    print(num)
