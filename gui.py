my_list=[
     [0,0,0,1,0,0,0],
     [0,0,1,1,1,0,0],
     [0,1,1,1,1,1,0],
     [1,1,1,1,1,1,1],
     [0,0,0,1,0,0,0],
     [0,0,0,1,0,0,0]

]
for i in my_list:
    for j in i:
        if j == 1:print("#",end=" ")
        else:print(" ",end=" ")
    print(" ")
