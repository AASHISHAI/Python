def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(a,'!=',fact)


fact(5)
    