print("Welcome Tanishq ❤️")
# Relational operators >,<,>=,<=,==,!= ->Boolean
# Logical operators -> and, or, not -> Boolean
# Bitwise operators -> &, |, ^, ~, <<, >> -> Binary 
# Assignment operators -> =, +=, -=, *=, /=, %=, **=, //=, &=
# name=input("enter your name = ")
# height1=int(input(f"enter your height {name} = "  ))
# name2=input("enter your name = ")
# height2=int(input(f"enter your height {name2}= "  ))
# if(height1>height2):
#   print(f"{name} is greater than {name2}")
# elif(height1==height2):
#   print(f"{name} and {name2} are of same height")
# else:
#   print(f"{name} is less than {name2}")

# Task 1
stock1 = "vanilla"
stock2 = "lime"
stock3 = "chocolate"

# Ask user their fav flavour


# Ouput
# Case1:
# "Yes, we do have it"

# Case2:  
#"No, we ran out of stock"
choice=input("enter your choice = ")
# if(choice==stock1 or choice==stock2 or  choice== stock3):
#   print("Yes, we do have it")
# else:
#   print("No, we ran out of stock")
  
# stock1 = "vanilla"
# stock2 = "lime"
# stock3 = "chocolate"
# flavor = input("What flavor of ice cream do you want? ")
# list = ["stock1","stock2","stock3"]
# if(flavor in list):
#   print("Yes, we do have it.")
# else:
#   print("No, we ran out of stock")

#in ->membership operator
shop_stock="vanilla, lime, chocolate"
# if(choice in shop_stock):
#   print("yes, we do have it")
# else:
#   print("No, we ran out of stock")

# ternary operator
# condition_if_true if condition else condition_if_false
# print("yes") if choice in shop_stock else print("No, we v")

output = "Yes" if choice in shop_stock else "No, we ran out of stock"
print(output)
