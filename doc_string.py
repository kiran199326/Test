#Doc String
def test(a):
    #Doc string
    '''
    This function returns some thing
    '''
    print(a)
help(test) #--> prints methods document
print(test.__doc__) # --> dunder method
