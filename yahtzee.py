#Yahtzee Game in Python

import random

reroll = 3          #number of rolls in a turn
rolled_dice = 5     #number of dice to roll
final_dice = []     #values to be given to the user at the end of a turn
dice_roll = [None]  #number of dice to roll after keeping dice
shown_dice = [None]

def rolldice(dice):  #function to randomly roll dice
    dice_roll = [None] * dice
    for i in range(dice):
        dice = random.randint(1,6)
        dice_roll[i] = dice
    dice_roll.sort()
    print(dice_roll)
    return dice_roll

def turn_roll(roll, re_roll):  #function to roll dice in a given reroll
    shown_dice = [None] * roll
    shown_dice = rolldice(roll)
    print("How many dice do you want to keep?")
    dice_keep = int(input())
    temp = [None] * dice_keep
    if dice_keep == 5:
        for x in range(dice_keep):
            temp[x] = shown_dice[x]
        final_dice.extend(temp)
    elif dice_keep < 5:
        for x in range(dice_keep):
            print("What are the values of the kept dice?")
            temp[x] = int(input())
        print("You kept these values")
        print(temp)
    elif dice_keep == 0:
        if re_roll == 1:
            for x in range(dice_keep):
                temp[x] = shown_dice[x]
            return
        else:
            print("Roll again? y/n")
            cont_roll = input()
            if cont_roll == "n":
                dice_keep = None   
    final_dice.extend(temp)
    if len(final_dice) == 5:
        dice_keep = None
    return [dice_keep, temp]
    

def sum_dice():
    sum = 0
    for s in range(len(final_dice)):
        sum += final_dice[s]
    return sum

  
#scorecard variables and functions
turn_count = 13 #number of turns in a game (default 13)
top_sum = 0    #sum of all the values at the top of the scorecard
bottom_sum = 0 #sum of all the values at the botttom of the scorecard
total_sum = 0  #sum of top and bottom sum which is end of game score

scorecard = [
    ["Ones", 0],
    ["Twos", 0],
    ["Threes", 0],
    ["Fours", 0],
    ["Fives", 0],
    ["Sixes", 0],
    ["3 of a Kind", 0],
    ["4 of a Kind", 0],
    ["Full House", 0],
    ["Small Straight", 0],
    ["Large Straight", 0],
    ["Yahtzee", 0],
    ["Chance", 0]
]

def scorecard_display():
    for i in range(6):
        print(str(i+1) + ") " + str(scorecard[i][0]) + " " + str(scorecard[i][1]))
    print("\n")
    for y in range(7):
        print(str(y+7) + ") " + str(scorecard[y+6][0]) + " " + str(scorecard[y+6][1])) 
        
        
#function for bottom scorecard to evaluate if the user met the requirement or not for the box            
def got_score():
    print("Did you get the score? y/n")
    score_got = input()
    if score_got == "n":
        scorecard[score][1] = 0
    return score_got
        
        
        
#start of the game               
while turn_count > 0:
    
    #first phase of the turn, rolling dice
    print("This is the first turn")
    while reroll > 0:
        print("You have " + str(reroll) + " roll(s) left.")
        
        dice_kept = turn_roll(rolled_dice, reroll)
        if dice_kept[0] == None:
            break
        rolled_dice = rolled_dice - dice_kept[0]
        reroll -= 1

    #end of phase 1  
    reroll = 3
    rolled_dice = 5 
    final_dice.append(dice_kept[1])
    print("The dice on the table are as follows:")
    print(final_dice)
    
    
    print("Here is your current scorecard:")
    scorecard_display()
        
    #second phase of the turn which is writing down score    
    print("What score do you want to put? Enter 1-13")
    score = int(input())

    #top scorecard things
    if score <= 6: 
        print("What is the value of the score?")
        value = int(input())

        scorecard[score-1][1] = value

    #bottom scorecard things
    else:
             
        if score == 7: #3 of a kind
            scorecard[6][1] = sum_dice() 
            got_score() 
        if score == 8: #4 of a kind
            scorecard[7][1] = sum_dice() 
            got_score()             
        if score == 9: #full house
            scorecard[8][1] = 25 
            got_score()  
        if score == 10: #small straight
            scorecard[9][1] = 30
            got_score()
        if score == 11: #large straight
            scorecard[10][1] = 40
            got_score()
        if score == 12: #yahtzee
            scorecard[11][1] = 50
            yahtzee = got_score()
            if yahtzee == "y":
                print("Congrats! You got a Yahtzee!")  
        if score == 13: #chance
            scorecard[12][1] = sum_dice()
            
    #end of turn things 
    final_dice.clear()          
    scorecard_display()            
    turn_count -= 1    
           
 



#end of game things
for x in range(6):
    top_sum += scorecard[x][1]

if top_sum >= 63:
    top_sum += 35

for z in range(7):
    bottom_sum += int(scorecard[z+6][1])

total_sum = top_sum + bottom_sum

print("Top Sum = " + str(top_sum))
print("Bottom Sum = " + str(bottom_sum))
print("Total Sum = " + str(total_sum)) 


        