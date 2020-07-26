#build a counter
# print([*range(1,100)]) --> agumented unpacking operator
my_list= [*range(0,100)]
counter=0
for item in my_list:counter+=1
print(counter)
