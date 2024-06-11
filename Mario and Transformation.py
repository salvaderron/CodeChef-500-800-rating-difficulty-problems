# cook your dish here
n=int(input())
for i in range(0,n):
    a=int(input())
    if a % 3 == 0:
        print('NORMAL')
    elif a % 3 == 1:
        print('HUGE')
    else:
        print('SMALL')
