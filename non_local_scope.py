#non local scope

def outer():
    x="outer_local"
    def inner():
        nonlocal x
        x="inner_local"
        print(f"inner def {x}")
    print(inner())
    print(f"Outer def {x}")
outer()
#Rule 1 : look for local scope i.e function scope
#Rule 2 : Look for parent function scope
#Rule 3 : Look for global scope
#Rule 5 : Look in for built in python function scope
