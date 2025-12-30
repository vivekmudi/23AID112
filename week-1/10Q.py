Temp_C=float(input("Enter temperature in the celsius: "))
Temp_F=(Temp_C*(9/5))+32
print(f"Temperature in Fahrenheit = {Temp_F}")
if Temp_C<0:
    print("Very cold! Wear thick jacket")
else:
    if Temp_C>=0 and Temp_C<=15:
        print("Cold. Wear jacket")
    else:
        if Temp_C>=16 and Temp_C<=25:
            print("Nice weather")
        else:
            print("Hot! Stay hydrated")