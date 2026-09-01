# I'm just learning loops in python

import random
New_Born_Eggs = 5

while New_Born_Eggs != 0:
    New_Born_Eggs -= 1
    print('Here we go!! From 5 to ' + str(New_Born_Eggs))

for random_thing in range(5):
    print('This thing became for now a count of ' + str(random_thing))

Random_Math_Trick = 0

for number in range(101):
    Random_Math_Trick = Random_Math_Trick + number
print('Its a magic trick! And you have ' + str(Random_Math_Trick))

for i in range(10):
    print(random.randint(0,11))

