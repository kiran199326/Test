#print highest even number form the my_list

def high_even(num):
    register=[]
    for i in num:
        if i % 2== 0:register.append(i)
    return f"Largest even number in list is {max(register)}"
print(high_even(list(range(100))))
