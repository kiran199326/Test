#global scope
a=10
"""
def test():
    a+=20 #UnboundLocalError: local variable 'a' referenced before assignment
print(test())
"""
def test():
    global a
    a+=20
    return a
test()
test()
print(test())

#or
def test1(a): ##injection
    a+=20
    return a
print(test1(test1(test1(a))))


#Rule 1 : look for local scope i.e function scope
#Rule 2 : Look for parent function scope
#Rule 3 : Look for global scope
#Rule 5 : Look in for built in python function scope
