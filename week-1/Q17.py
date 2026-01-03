num_list=[]
for i in range(8):
    list=int(input("Enter a value which is in between the range(1,100):"))
    num_list.append(list) # using random library we can create the list
print(num_list)
# Biggest and smallest numbers in the list
big=0
for var in range(8):
    if(num_list[var]>big):
      big=num_list[var]
    else:
        small=num_list[var]
print(f"Biggest and smallest numbers in the list are {big} and {small}")
