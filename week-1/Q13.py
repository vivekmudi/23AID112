list =["Pizza","Sushi","Eggs","Paneer","milk","fruitJuice"]
for i in range(0,6):
    print(f"{i+1}. {list[i]}")  #here it prints vertically ,if u want horizontal use end=""
for i in range(0,6):
    print(f"{i+1}. {list[i]}" , end=" " )
