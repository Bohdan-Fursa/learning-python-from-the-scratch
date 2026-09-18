# Its just simple program where asking your age and retruns to you that you old, or young, or a kid

print("Welcome! Type your age here: ")

age = input("> > >")

age = int(age)

if age > 60:
    print("You old.")
elif age <= 10:
    print("You just a kid.")
elif age >= 100:
    print("You a vampire.")
elif age >= 18:
    print("You adult.")
