#Author: George Sigety

import random

def is_increasing(three_roll):
    if three_roll[0] < three_roll[1]:
        if three_roll[1] < three_roll[2]:
            return True
    return False



# 6 sides of a die held in an array:
sides = [1, 2,  3, 4, 5, 6]
#set the arrays to hold the 10^6 sequences of 3 die rolls
three_roll = [0,0,0]
rolls = [None] * 10**6
i = 0
no_increasing = 0
#fill the array with 10^6 sequences of 3 random die rolls
while i < 10**6:
    x = 0
    while x < 3:
        three_roll[x] = random.choice(sides)
        x += 1
    #count the number of 3 rolls that are increasing
    if (is_increasing(three_roll)):
        no_increasing += 1
    three_roll = [0,0,0]
    i += 1

# solve for the probability using |E|/|S|
probability_increasing = no_increasing / 10**6

#print the probability
print(probability_increasing)