list=[12,45,3,98,7,34,21]
print("list of all numbers")
for i in range(0,7):
    print(f"{list[i]}",end=" " )
print("\nnumbers greater than 30 in the list")
count=0
for i in range(0, 7):
    if(list[i]>30):
        print(f"{list[i]}",end=" ")
        count+=1
print(f"\n{count} numbers that are greater than 30")
