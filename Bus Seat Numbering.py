# cook your dish here
n=int(input())
for i in range(0,n):
    a=int(input())
    if a>=1 and a<=15:
        if a>=1 and a<=10:
            print("Lower Double")
        else:
            print("Lower Single")
    else:
        if a>=16 and a<=25:
            print("Upper Double")
        else:
            print("Upper Single")
