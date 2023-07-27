import random

count = []
test = [None] * 5
counter = 0
finish = 0
num = 0
i = 1


def rolldice(dice):  #function to randomly roll dice
    dice_roll = [None] * dice
    for i in range(dice):
        dice = random.randint(1,6)
        dice_roll[i] = dice
    # print(dice_roll)
    return dice_roll


while i > 0:
    for x in range(10):
        while finish < 1:
            yahtzee = rolldice(5)
            yahtzee.sort()
            test = [yahtzee[0]] * 5
            if yahtzee == test:
                break
            counter += 1
            num += 1
        count.append(counter)
        counter = 0

    count.sort()       
    for z in range(len(count)):
        if count[z] == 1:
            print("Congrats! It only took one try to get a yahtzee.")
            print("It took " + str(num) + " number of tries.")
            for x in range(len(count)):
                print(count[x]) 
            i = 0
            num = 0
    count.clear()     
    


