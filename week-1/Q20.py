shopping_list=[]
while True:
    choose=input("Choose anything from these (add,remove,show or quit):")
    if choose=="add":
        list=input("Enter the item name:")
        shopping_list.append(list)
        print(list)
    elif choose=="remove":
        item=input("Enter the item name to remove")
        if item in shopping_list:
          shopping_list.remove(item)
          print(f"updated list {shopping_list}")
        else :
          print("item is not found in shopping list")
    elif choose=="show":
        print(f"current shopping lis is {shopping_list}")
    elif choose=="quit":
        break
