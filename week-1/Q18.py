Secret_number = 7
while True:
    guess = int(input("Enter a number:"))
    if guess != Secret_number:
        if guess>Secret_number:
          print('"Too high"')
        else:
           print("Too low")
    else:
        print(f"your guess is right,it is {guess}")
        break