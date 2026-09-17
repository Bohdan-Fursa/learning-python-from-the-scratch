#  It will be simple game, its raining and you need to go to shop. and you need make a choices.


print("Its just raining outside, you need to go to shop to buy some kind of stuff")
print("First of all, do you wanna take umbrella with you?")
print("For all choices, to agree type 1 and 0 if you dont")
choice = input("Time has come > > >")

if choice == "1":
    print("Good now you dont will be get wet in the rain")
    print(
        "You see two difirent ways, you wanna go like you go usually? Or go difirent way, its look some kind of scary.."
    )
    choice = input("Time has come > > >")
    if choice == "1":
        print("You choose your ordinary way to shop and you see some kind of monster")
        print("He kills you. You dead")
    else:
        print(
            "You go another way, that looks scary but you see just a cat before your eyes."
        )
        print("You take him with you and now you have a cat.")
        print("The end.")
else:
    print("You dont take umbrella with you and monster see it..")
    print("You died. Because monster dont like unusually things from people")


#  In Episode 2 i just study how to use if-else statment.
#  if - there i give the condition
#  else - that what was difirent from condition
#  elif - if i wanted to do else but set a condition
