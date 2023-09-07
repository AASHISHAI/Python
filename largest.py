'''l1=[1,4,5,6,7,9,200]
large=1
n=len(l1)
for i in range(n):
    for j in range(n):
         if (l1[i]<l1[j]):
             large=l1[j]
print(large)'''

l1=[1,4,5,6,7,9,200]
l1.sort()
print(l1[-1])