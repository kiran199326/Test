#Duplicates in list
some_list = ['a','b','c','d','e','f','g','h','a','b','c','d']
new_list=[]
for key in some_list:
    if some_list.count(key) > 1:
        if key not in new_list:new_list.append(key)
print(new_list)
