def sum(num1 , num2):return(num1 + num2)
print(sum(6,5))
#return exits function
# Nested functions
def sum1(n1 , n2):
    def sum2(n4 , n5):
        return n4 + n5
    return sum2(n1,n2)
    print("blah")#will not work since the above return killed it !!
print(sum1(7 , 8))
