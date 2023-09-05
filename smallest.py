'''l1=[1,8,7,4,5]
small=0
n=len(l1)
for i in range(n):
    for j in range(n):
     if l1[i]>l1[j]:
      small=l1[j]
print(small)'''

l1=[1,8,7,4,5]
l1.sort()
print(l1[0])