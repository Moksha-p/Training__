def fibbo(n):
    a = 0
    print(a)
 
    b = 1
    if n>1:
        print(b)
    i = 2
    while i<n:  
        c = a+b
        print(c)
        a = b 
        b = c
        i = i + 1
fibbo(5)