#Diego Espinola
#10.23.19
#craps program1

import random

def create():
    print("Welcome, to start te game you need to add money to your bank")
    print("Enter the amount of money you want in your bank\n>")
    return int(input())

def money_bet():
    print("Enter the amount of money you want to bet\n>")
    return int(input())

def roll_dice():
    roll= random.randint(1,12)
    print(f"You have rolled {roll}")
    return roll

def play_game():
    bank = create()
    bet = money_bet()
    dice = roll_dice()
    if dice == 7 or dice == 11:
        print("You won!")
        bank = bank + bet
        print(f"You have {bank}")
    elif dice == 2  or dice == 3 or dice == 12:
        print("You lost")
        bank = bank - bet
        print(f"You have {bank}")
    else:
        print(f"You have made point with {dice}, now you need to roll that number to win")
        point = dice
        dice= random.randint(1,12)
        if(dice == point):
            bank= bank + bet
            print(f"You won, you rolled {dice}. Now you have {bank}")
        else:
            bank= bank - bet
            print(f"You have lost, you rolled {dice}.You have {bank}")
    print("Would you like to play again? Y or N?")
    choice = input()

    if choice == "Y":
        print(f"How much you want to bet from your {bank}?")
        bet= int(input())
        dice = roll_dice()
    if dice == 7 or dice == 11:
        print("You won!")
        bank = bank + bet
        print(f"You have {bank}")
    elif dice == 2  or dice == 3 or dice == 12:
        print("You lost")
        bank = bank - bet
        print(f"You have {bank}")
    else:
        print(f"You have made point with {dice}, now you need to roll that number to win")
        point = dice
        dice= random.randint(1,12)
        if(dice == point):
            bank= bank + bet
            print(f"You won, you rolled {dice}. Now you have {bank}")
        else:
            bank= bank - bet
            print(f"You have lost, you rolled {dice}.You have {bank}")
    print("Would you like to play again? Y or N?")
    choice = input()

    if ( bet > bank):
            print("You dont have that money available,the game will end.")
            bet = 0
    else:
        print("Bye Bye")
        bet = 0


play_game()




