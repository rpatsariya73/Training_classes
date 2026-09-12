def swap(a:int , b:int)->None:
    a = a+b
    b = a-b
    a = a-b
    print(a,b)
swap(5,6)  