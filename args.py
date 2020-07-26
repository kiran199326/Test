#*args and **kwargs --> keyword arguments

#def test(args): Fails since can not on multiple values
def test(*args): #works on multiple args
    print(args)
    return(sum(args))
print(test(1,2,3,4,5))

def test1(*args,**kwargs): #works on multiple args
    print(kwargs)
    total=0
    for tot in kwargs.values():
        total+=tot
    return sum(args , total)
print(test1(1,2,3,4,5,n1=5,n2=10))
