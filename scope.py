#scope
a=1
def con():
    a=5
    print(f"a in def not overridden by global {a}")
    #global a
    #print(f"a in def overridden by global {a}")
print(f"a not in def {a}")
print(con())

def test():
    def test1():
        return sum
    return test1()
print(test())

#Rule 1 : look for local scope i.e function scope
#Rule 2 : Look for parent function scope
#Rule 3 : Look for global scope
#Rule 5 : Look in for built in python function scope
