# This is show possibles of python with numbers

print('Welcome to the python, 2 program, I wanted to show you, what python can do with numbers')
User_Number = int(input('Input here your number > > > '))
print('Ok good choice your number ' + str(User_Number))
print('Now what you wanna do with it? Press 1-3, to action')
print('1.Just round')
print('2.Round down')
print('3.Just give me float')
action = input('> > > ')

print('You choose ' + str(action))

if action == '1':
    User_Number = round(User_Number)
    print("Process round successfully completed")
elif action == '2':
    User_Number = int(User_Number)
    print("Process int was do own way")
elif action == '3':
    User_Number = float(User_Number)
    print('Maybe float not just a way but a thing')

print('We doing the great stuff, because of action you choose ' + str(action) + " and now you have this number " + str(User_Number))

