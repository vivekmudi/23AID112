num_list=[]
for i in range(1,21):        # or u can create directly using num_list=list(range(1,21))
    list=i
    num_list.append(list)
print(num_list) # list is created
print("Numbers that are divisible by 3 are")
for i in range(0,20):
    if num_list[i]%3==0:
        print(num_list[i])
