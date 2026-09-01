import random
import sys

# This is just random game what I have done while learning python, for fun...

pythonic_code = ['print()', 'while', 'for', 'if','else']


while True:
    print('Hello to new game, that i just was came up with, and I wanna show you what a simple python game can do to you')
    print('This is playground game, where you need to choose simple number, float, or just integer, what ever you want and if you have a pure of luck you can win the scores')
    print('With scores you can exchange it to random pythonic code, that would be your prise for wining')
    print('Important Rule, dont cheat please, and 100 score is the price for exchange, wish you good luck')

    User_Choose_The_Number = input('Waiting your chance! > > > ')


    print('Ok, you sure you wanna chose that number?')
    print('Press 1 to reduce your choice and 2 if you accepted your further')

    Sure_Or_Not = input('> > > ')

    if Sure_Or_Not == '2':
        print('Wish you good luck, choice was confirmed')
    else:
        print('Ok, we will be start again, how you wish')
        continue

    Number_Of_Luck = 0
    score = 0
    def game_chance():
        print('Lets roll the game!!')
        print('Your chance now loading... ')
        for i in range(Number_Of_Luck):
            score = random.randint(0,100)
        print('Score just choose their fate ')
        if score < 50:
            print('Maybe you need try more chance...')
        elif score > 60 < 80:
            print('You have done well.. great!')
        elif score == 100:
            print('JUST A JACKPOT!!!')
            print('CONGRATULATIONS!!! YOU JUST A MACHINE OF LUCK!!')
        print('Score just was, just like a fate wish for you ' + str(score))

    def ask_user_about_repeat():
        print('Do you wanna play again?')
        print('Press 1, if you agree and 2 if you wanna exit')

        hard_choice = input('> > > ')

        if hard_choice == '1':
            print('Then lets go again!!')
            if score == 100:
                print('Before we started, you wanna exchange your 100 score for random python code?')
                print('Press 1 if you agree and 2 if you dont')
                if input('> > > ') == '1':
                    print('And now you have this! ' + random.choice(pythonic_code))
                else:
                    print('Ok, how you wish..')
        else:
            print('Bye then..')
            sys.exit()




    if '.' in User_Choose_The_Number:
        User_Choose_The_Number = float(User_Choose_The_Number)
        print('Ok, we got it you have the float number! YOU JUST A MATHEMATICS MACHINE!!!')
        print('Chance was increased!!')
        Number_Of_Luck = random.randint(0,100)
        print('Your luck now is ' + str(Number_Of_Luck))
        game_chance()
        ask_user_about_repeat()
    else:
        print('Ok, you have a number, maybe you dont like this ".", i get it...')
        print('But luck maybe be on another side....')
        Number_Of_Luck = random.randint(0,35)
        game_chance()
        ask_user_about_repeat()



