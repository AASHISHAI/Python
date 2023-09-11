'''Calculate the sum of all number from 1 to n. Accept 'n'from user n is an integer value'''
n=int(input('enter the number :'))
sum=0
for i in range(1 ,n+1):
    sum=sum+i
    print(sum)