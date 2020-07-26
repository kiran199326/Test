my_list=[
     [0,0,0,1,0,0,0],
     [0,0,1,1,1,0,0],
     [0,1,1,1,1,1,0],
     [1,1,1,1,1,1,1],
     [0,0,0,1,0,0,0],
     [0,0,0,1,0,0,0]
]
for row in my_list:
    for pixel in row:
        if pixel == 1:print("#",end=" ")
        else:print(" ",end=" ")
    print(" ")
