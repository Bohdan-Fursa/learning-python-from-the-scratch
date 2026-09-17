# Here we have a normal calulator, where you can input two numbers and choice what you wanna do with it.


print("Welcome to Calculator! Type two numbers and choice what you wanna do.")
number_one = input("> > >")
number_two = input("> > >")

number_one = int(number_one)
number_two = int(number_two)

print("Now choice what you wanna do with this two.")
print("1 - addition. 2 - division. 3 - multiplication. 4 - subtraction")

choice = input("> > >")

if choice == "1":
    sum = number_one + number_two
elif choice == "2":
    sum = number_one / number_two
elif choice == "3":
    sum = number_one * number_two
elif choice == "4":
    sum = number_one - number_two

print("Here what yo have: " + str(sum))
