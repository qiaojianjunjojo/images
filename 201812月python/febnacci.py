def feb(n):
    a=0
    b=1
    for i in range(n): 
        b,a=a+b,b
        print(a)

feb(20)
