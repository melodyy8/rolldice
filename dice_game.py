#helper functions for dice game
import random
import sys
from playsound import playsound

#returns a list of n rolled 6-dice, n >= 0
def list_dice(n):
    if (n < 0):
        print("Invalid input!")
        sys.exit()
    return [random.randint(1, 6) for  x in range(n)]

#returns a list of n rolled k-dice, n >= 0 and k >= 1
def list_kdice(n, k):
    if (k < 1 or n < 0):
        print("Invalid input!")
        sys.exit()
    return [random.randint(1, k) for x in range(n)]

#sums a list of dice values
def sum_dice(l):
    if (not l):
        print("Invalid input!")
        sys.exit()
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum

#takes the average of a list of dice values
def avg_dice(l):
    s = sum_dice(l)
    avg = (s / len(l))
    return avg

#rolls n 6-dice and returns their sum
def roll_dice(n):
    l = list_dice(n)
    return sum_dice(l)

#rolls n k-dice and returns their sum
def roll_kdice(n, k):
    l = list_kdice(n, k)
    return sum_dice(l)

player_amount = 1000
print("Welcome to RollDice! A fun dice game!")
print("In this game, you will play by rolling dice against the computer!")
print("The game ends once you earn $1 million, or if you run out of money.")
print("Have fun!")
while True:
    print("You currently have " + str(player_amount) + ".")
    print("How much do you want to bet? (If you don't want to play anymore, type 'I'm done')")
    bet_amount = input("Bet: ")
    if bet_amount == "I'm done":
        print("Thanks for playing! :)")
        break
    bet_amount = int(bet_amount)
    print("How many dice do you want to roll?")
    dice_num = int(input("Dice: "))
    player_sum = sum_dice(list_dice(dice_num))
    comp_sum = sum_dice(list_dice(dice_num))
    if player_sum > comp_sum:
        print("The sum of your rolled dice is", player_sum, "and the sum of your opponent's rolled dice is", str(comp_sum) + ". You won " + str(bet_amount) + ", yay!")
        player_amount += bet_amount
    elif player_sum < comp_sum:
        print("The sum of your rolled dice is", player_sum, "and the sum of your opponent's rolled dice is", str(comp_sum) + ". You lost " + str(bet_amount) + ", sorry.")
        player_amount -= bet_amount
    else:
        print("The sum of your rolled dices is", player_sum, "and the sum of your opponent's rolled dices is", str(comp_sum) + ". It's a tie!")
    if  player_amount <= 0:
        print("You ran out of money, sorry. Better luck next time!")
        break
    elif player_amount >= 1000000:
        print("You earned more than 1 million dollars! You won, congratulations!!")
        break