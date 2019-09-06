#Sequence Game
#Author : Taekyung, Kil ( #000799798 )
# 07/April / 2019


import random
import time

ran = random.randint(10000, 30000)

price = []
print (ran)
ran = str(ran)


for i in ran:
    i = str(i)
    price.append(i)

print("Bob Meower says, 'Today we're playing Three Strikes, reach in the \n                  bag and pull out a ball to get us started.'")



print ("Bob Meower says, You drew the ball with the number " + price[3])

position = input("Bob Meower asks, 'Which position, does this number belong in? (first position is '0')(start to 0 ) ' : ")
time.sleep(0.2)
while True:
    if not (position.isnumeric()):
        position=input("Bob Meower says, 'I couldn't make that out, please pick a number from 1-5 nice and clearly for us.'")
        

    else :
        break
        
while True:

    if not (price[int(position)] == price [3]):
        position = input("Bob Meower asks, It is wrong. Please pick again :  ")
        time.sleep(0.2)

    else :
        print("Bob Meower says, That's correct.")
        print("Bob Meower says, Pick another ball, let's win a car!")
        break



print ("Bob Meower says, You drew the ball with the number " + price[0])
time.sleep(0.2)
position1 = input("Bob Meower asks, 'Which position, does this number belong in? (start to 0 ) ' : ")
time.sleep(0.2)



while True:
    if not (position1.isnumeric()):
        position1=input("Bob Meower says, 'I couldn't make that out, please pick a number from 1-5 nice and clearly for us.'")
        

    else :
        break
    
while True:

    if not (price[int(position1)] == price [0]):
        position1 = input("Bob Meower asks, It is wrong. Please pick again :  ")
        time.sleep(0.2)

    else :
        print("Bob Meower says, That's correct.")
        print("Bob Meower says, Pick another ball, let's win a car!")
        break

print ("Bob Meower says, You drew the ball with the number " + price[1])
position2 = input("Bob Meower asks, 'Which position, does this number belong in? (start to 0 ) ' : ")
time.sleep(0.2)

while True:
    if not (position2.isnumeric()):
        position2=input("Bob Meower says, 'I couldn't make that out, please pick a number from 1-5 nice and clearly for us.'")
        

    else :
        break
while True:

    if not (price[int(position2)] == price [1]):
        position2 = input("Bob Meower asks, It is wrong. Please pick again :  ")
        time.sleep(0.2)
    else :
        print("Bob Meower says, That's correct.")
        print("Bob Meower says, Pick another ball, let's win a car!")
        break

print ("Bob Meower says, You drew the ball with the number " + price[2])
position3 = input("Bob Meower asks, 'Which position, does this number belong in? (start to 0 ) ' : ")
time.sleep(0.2)

while True:
    if not (position3.isnumeric()):
        position=input("Bob Meower says, 'I couldn't make that out, please pick a number from 1-5 nice and clearly for us.'")
        time.sleep(0.2)

    else :
        break
while True:

    if not (price[int(position3)] == price [2]):
        position = input("Bob Meower asks, It is wrong. Please pick again :  ")

    else :
        print("Bob Meower says, That's correct.")
        print("Bob Meower says, Pick another ball, let's win a car!")
        break

print ("Bob Meower says, You drew the ball with the number " + price[4])
position4 = input("Bob Meower asks, 'Which position, does this number belong in? (start to 0 ) ' : ")
time.sleep(0.2)

while True:
    if not (position4.isnumeric()):
        position4=input("Bob Meower says, 'I couldn't make that out, please pick a number from 1-5 nice and clearly for us.'")
        time.sleep(0.2)

    else :
        break
while True:

    if not (price[int(position4)] == price [4]):
        position4 = input("Bob Meower asks, It is wrong. Please pick again :  ")

    else :
        break
time.sleep(0.3)
print("Bells ring, lights flash, and Bob Meower turns and exclaims \n           'You've done it! That car is all yours'")
print("Bob Meower exclaims 'You correctly guessed the retail price of $" + ran)
